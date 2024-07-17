from flask import render_template


def render_all_inspections(user, qc, username):
    return render_template('quality_template.html', user=user, qc=qc, username=username)
