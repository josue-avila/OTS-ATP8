from flask import Blueprint, render_template

from backend.controllers.log_controller import LogController

logs = Blueprint('log', __name__)

log_controller = LogController()


@logs.route('/logs', methods=["GET", "POST"])
def list_logs():
    logs = log_controller.read_all()
    return render_template('list_log.html', title='Logs', list=logs)
