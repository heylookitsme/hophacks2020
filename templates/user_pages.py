import flask
from flask import request, jsonify, render_template, Blueprint
from flask_login import login_required, current_user

up = Blueprint('up',  __name__,  template_folder='templates')

@up.route('/projects/hophacks2020/supplies', methods=['POST'])
@login_required
def supplies():
	
	#keeping json around for future extensibility of public supplies, or secondary uses
	tempdict = { "gloves" : current_user.gloves, "cloth" : current_user.cloth, "surgical" : current_user.surgical, "sanitizer" :current_user.sanitizer}
	
	return render_template("supplies.html", json.dumps(tempdict))
