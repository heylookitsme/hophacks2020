from flask import request, jsonify, render_template, Blueprint
from flask_login import login_required, current_user
import json

up = Blueprint('up',  __name__,  template_folder='templates')

@up.route('/supplies')
@login_required
def supplies():
    
	#keeping json around for future extensibility of public supplies, or secondary uses
	tempdict = { "gloves" : current_user.gloves, "cloth" : current_user.cloth, "surgical" : current_user.surgical, "sanitizer" :current_user.sanitizer}
	
	return jsonify(tempdict) #"render_template("supplies.html", json.dumps(tempdict))

@up.route('/supplies', methods=['POST'])
@login_required
def supp_edit():
	#WIP
	return "ahem, ******************"
