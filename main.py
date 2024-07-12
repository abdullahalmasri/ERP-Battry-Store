from flask import Flask, request, redirect, url_for, session, render_template, jsonify

from controllers.battery_controller import BatteryController
from controllers.order_controller import OrderController
from controllers.quality_controller import QualityController
from controllers.recycling_controller import RecyclingController
from controllers.remanufacturing_controller import RemanufacturingController
from controllers.report_controller import ReportController
from controllers.supplier_controller import SupplierController
from controllers.user_controller import UserController
from models.battery import Battery
from views.battery_view import render_battery_details, render_all_batteries
from views.order_view import render_order_details, render_all_orders
from views.quality_view import render_inspection_details, render_all_inspections
from views.recycling_view import render_process_details as render_recycling_details, \
    render_all_processes as render_all_recycling_processes
from views.remanufacturing_view import render_process_details as render_remanufacturing_details, \
    render_all_processes as render_all_remanufacturing_processes
from views.report_view import render_report_details, render_all_reports
from views.supplier_view import render_supplier_details, render_all_suppliers
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
    battery = Battery(1, 'good', 1, 'cold')
    battery_controller.add_battery(battery)
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
    battery = battery_controller.find_battery_by_id(battery_id)
    if battery:
        return render_battery_details(battery)
    return jsonify({"error": "Battery not found"}), 404


@app.route('/suppliers')
def suppliers():
    return render_all_suppliers(supplier_controller.suppliers)


@app.route('/suppliers/<int:supplier_id>')
def supplier(supplier_id):
    supplier = supplier_controller.find_supplier_by_id(supplier_id)
    if supplier:
        return render_supplier_details(supplier)
    return "Supplier not found."


@app.route('/orders')
def orders():
    return render_all_orders(order_controller.orders)


@app.route('/orders/<int:order_id>')
def order(order_id):
    order = order_controller.find_order_by_id(order_id)
    if order:
        return render_order_details(order)
    return "Order not found."


@app.route('/remanufacturing_processes')
def remanufacturing_processes():
    return render_all_remanufacturing_processes(remanufacturing_controller.processes)


@app.route('/remanufacturing_processes/<int:process_id>')
def remanufacturing_process(process_id):
    process = remanufacturing_controller.find_process_by_id(process_id)
    if process:
        return render_remanufacturing_details(process)
    return "Remanufacturing process not found."


@app.route('/recycling_processes')
def recycling_processes():
    return render_all_recycling_processes(recycling_controller.processes)


@app.route('/recycling_processes/<int:process_id>')
def recycling_process(process_id):
    process = recycling_controller.find_process_by_id(process_id)
    if process:
        return render_recycling_details(process)
    return "Recycling process not found."


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
    report = report_controller.find_report_by_id(report_id)
    if report:
        return render_report_details(report)
    return "Report not found."


@app.route('/logout')
def logout():
    username = request.args.get('username', '')
    logout_message = user_controller.logout_user(username)
    return render_login_view(error=logout_message)


if __name__ == "__main__":
    app.run(debug=True, port=9000)
