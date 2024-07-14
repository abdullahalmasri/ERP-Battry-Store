from flask import Flask, request, redirect, url_for, session, jsonify, render_template, flash

from controllers.battery_controller import BatteryController
from controllers.order_controller import OrderController
from controllers.quality_controller import QualityController
from controllers.recycling_controller import RecyclingController
from controllers.remanufacturing_controller import RemanufacturingController
from controllers.report_controller import ReportController
from controllers.supplier_controller import SupplierController
from controllers.user_controller import UserController
from models.battery import Battery
from models.recycling_process import RecyclingProcess
from models.remanufacturing_process import RemanufacturingProcess
from models.supplier import Supplier
from views.battery_view import render_battery_details, render_all_batteries
from views.order_view import render_all_orders
from views.quality_view import render_inspection_details, render_all_inspections
from views.recycling_view import render_all_processes as render_all_recycling_processes
from views.remanufacturing_view import render_all_processes as render_all_remanufacturing_processes
from views.report_view import render_report_details, render_all_reports
from views.supplier_view import render_all_suppliers
from views.user_view import render_login_view, render_dashboard_view

app = Flask(__name__, template_folder='views')  # Ensure the template folder is 'views'
app.secret_key = 'your_secret_key'
user_controller = UserController()
battery_controller = BatteryController()
supplier_controller = SupplierController()
order_controller = OrderController()
remanufacturing_controller = RemanufacturingController()
recycling_controller = RecyclingController()
quality_controller = QualityController()
report_controller = ReportController()

# Add example users
user_controller.add_user(3, "a", "a", "administrator")


# user_controller.add_user(2, "john_doe", "password456", "regular")

@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = user_controller.authenticate_user(username, password)
        if user:
            print('this is the user ', user)
            session['user_id'] = user.user_id
            session['username'] = user.username
            session['role'] = user.role
            return redirect(url_for('dashboard', username=user.username))
        else:
            return "Invalid credentials. Please try again."
    return render_login_view()


@app.route('/dashboard/<username>', methods=['GET'])
def dashboard(username):
    if 'username' not in session or session['username'] != username:
        return redirect(url_for('login'))
    print('i am the ', username)
    newBattery = Battery(1, 'good', 1, 'cold')
    battery_controller.add_battery(newBattery)
    return render_dashboard_view(username, 'Hope have Great Day!')


@app.route('/batteries')
def batteries():
    username = request.args.get('username')
    batteries_list = [
        Battery('12345', 'Active', 100, 'Cool and dry place'),
        Battery('67890', 'Inactive', 50, 'Room temperature'),
        Battery('11223', 'Active', 75, 'Cool and dry place'),
    ]
    return render_all_batteries(batteries_list, username=username)


@app.route('/batteries/<int:battery_id>')
def battery(battery_id):
    # username = request.args.get('username')
    getBattery = battery_controller.find_battery_by_id(battery_id)
    if getBattery:
        return render_battery_details(getBattery)
    return jsonify({"error": "Battery not found"}), 404


@app.route('/suppliers')
def suppliers():
    username = request.args.get('username')
    return render_all_suppliers(supplier_controller.suppliers, username)


@app.route('/suppliers/<int:supplier_id>')
def supplier(supplier_id):
    supplier = supplier_controller.find_supplier_by_id(supplier_id)
    if supplier:
        return jsonify(supplier.__dict__)
    return jsonify({'message': 'Supplier not found'}), 404


@app.route('/orders')
def orders():
    username = request.args.get('username')
    print(username)
    return render_all_orders(order_controller.orders, username=username)


@app.route('/suppliers', methods=['POST'])
def add_supplier():
    data = request.get_json()
    new_supplier_id = len(supplier_controller.suppliers) + 1
    new_supplier = Supplier(
        supplier_id=new_supplier_id,
        name=data['name'],
        contact_info=data['contact_info'],
        performance_rating=data['performance_rating']
    )
    supplier_controller.add_supplier(new_supplier)
    return jsonify({'message': 'Supplier added successfully'}), 200


@app.route('/order', methods=['POST'])
def add_order():
    data = request.get_json()
    order_controller.place_order(data)
    return jsonify({'message': 'Order added successfully'}), 200


@app.route('/update_order_status', methods=['POST'])
def update_order_status():
    data = request.get_json()
    order_id = data.get('order_id')
    new_status = data.get('status')
    order = order_controller.find_order_by_id(order_id)
    if order:
        order.update_order_status(new_status)
        return jsonify({'message': 'Order status updated successfully'}), 200
    else:
        return jsonify({'error': 'Order not found'}), 404


@app.route('/track_order', methods=['POST'])
def track_order():
    data = request.get_json()
    order_id = data.get('order_id')
    order = order_controller.find_order_by_id(order_id)
    if order:
        newDate = order.track_delivery()
        return jsonify({'date': newDate}), 200
    else:
        return jsonify({'error': 'Order not found'}), 404


@app.route('/suppliers/<int:supplier_id>', methods=['PUT'])
def update_supplier(supplier_id):
    data = request.get_json()
    supplier_controller.update_supplier(
        supplier_id=supplier_id,
        name=data['name'],
        contact_info=data['contact_info'],
        performance_rating=data['performance_rating']
    )
    return jsonify({'message': 'Supplier updated successfully'}), 200


@app.route('/remanufacturing_processes')
def remanufacturing_processes():
    username = request.args.get('username')
    print(username)
    return render_all_remanufacturing_processes(remanufacturing_controller.processes, username)


@app.route('/remanufacturing_processes/<int:process_id>')
def remanufacturing_process(process_id):
    process = remanufacturing_controller.find_process_by_id(process_id)
    if process:
        return jsonify(process.__dict__)
    return "Remanufacturing process not found."


@app.route('/remanufacturing_processes/update/<int:process_id>', methods=['PUT'])
def update_remanufacturing_process(process_id):
    data = request.get_json()
    remanufacturing_processes = RemanufacturingProcess(
        process_id=process_id,
        battery_id=data['battery_id'],
        start_date=data['start_date'],
        end_date=data['end_date'],
        status=data['status']
    )
    remanufacturing_controller.update_process(remanufacturing_processes)
    return jsonify({'message': 'Remanufacturing process updated successfully'}), 200


@app.route('/add_remanufacturing_process', methods=['POST'])
def add_process():
    data = request.get_json()
    new_process_id = len(remanufacturing_controller.processes) + 1
    new_remanufacturing = RemanufacturingProcess(
        process_id=new_process_id,
        battery_id=int(data['battery_id']),
        start_date=data['start_date'],
        end_date=data['end_date'],
        status=data['status']
    )
    remanufacturing_controller.schedule_process(new_remanufacturing)
    return jsonify({'message': 'Remanufacturing process scheduled successfully'}), 200


@app.route('/recycling_processes')
def recycling_processes():
    username = request.args.get('username')
    processes = [process.__dict__ for process in recycling_controller.processes]
    return render_all_recycling_processes(processes, username)


@app.route('/recycling_processes/<int:process_id>')
def recycling_process(process_id):
    process = recycling_controller.find_process_by_id(process_id)
    if process:
        return jsonify(process.__dict__)
    return jsonify({"message": "Recycling process not found."}), 404


@app.route('/recycling_processes', methods=['POST'])
def add_recycling_process():
    data = request.json
    new_process = RecyclingProcess(
        process_id=data['process_id'],
        battery_id=data['battery_id'],
        start_date=data['start_date'],
        end_date=data['end_date'],
        status=data['status']
    )
    recycling_controller.plan_process(new_process)
    return jsonify({"message": "Recycling process added successfully."})


@app.route('/recycling_processes/<int:process_id>', methods=['PUT'])
def update_recycling_process(process_id):
    data = request.json
    status = data['status']
    recycling_controller.update_process_status(process_id, status)
    return jsonify({"message": "Recycling process updated successfully."})


@app.route('/inspections')
def inspections():
    return render_all_inspections(quality_controller.quality_controls)


@app.route('/inspections/<int:qc_id>')
def inspection(qc_id):
    qc = quality_controller.find_quality_control_by_id(qc_id)
    if qc:
        return render_inspection_details(qc)
    return "Inspection not found."


@app.route('/reports')
def reports():
    return render_all_reports(report_controller.reports)


@app.route('/reports/<int:report_id>')
def report(report_id):
    getReport = report_controller.find_report_by_id(report_id)
    if getReport:
        return render_report_details(getReport)
    return "Report not found."


@app.route('/aboutUs/<username>')
def about_us(username):
    return render_template('aboutUs.html', username=username)


@app.route('/contactUs/<username>', methods=['GET', 'POST'])
def contact_us(username):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Here you would normally handle the form submission,
        # such as sending an email or saving the feedback to a database.
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact_us', username=username))
    return render_template('contactUs.html', username=username)


@app.route('/logout')
def logout():
    username = request.args.get('username', '')
    logout_message = user_controller.logout_user(username)
    return render_login_view(error=logout_message)


if __name__ == "__main__":
    app.run(debug=True, port=9000)
