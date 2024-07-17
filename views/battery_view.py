from flask import render_template, jsonify


def render_battery_details(battery):
    return jsonify({
            'battery_id': battery.battery_id,
            'status': battery.status,
            'quantity': battery.quantity,
            'storage_conditions': battery.storage_conditions
        })


def render_all_batteries(user, batteries, username):
    return render_template('battery_Storage.html', user=user, batteries=batteries, username=username)
