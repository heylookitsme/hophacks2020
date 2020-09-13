from flask import request, jsonify, render_template, Blueprint, redirect, url_for
from flask_login import login_required, current_user
from . import db
import json

up = Blueprint('up',  __name__,  template_folder='templates')


@up.route('/supplies')
def supplies():
    
	if not current_user.is_authenticated:
		return redirect(url_for('um.login'))

	#keeping json around for future extensibility of public supplies, or secondary uses
	tempdict = { "gloves" : current_user.gloves, "cloth" : current_user.cloth, "surgical" : current_user.surgical, "sanitizer" :current_user.sanitizer}
	with open("hophacks2020/static/supplied.json", "w") as outfile: 
		 outfile.write(json.dumps(tempdict))
	return render_template("supplies.html") #jsonify(tempdict) #"render_template("supplies.html", json.dumps(tempdict))

@up.route('/supplies', methods=['POST'])
def supp_edit():

	gloves = request.form.get('gloves')
	cloth = request.form.get('cloth')
	surgical = request.form.get('surgical')
	sanitizer= request.form.get('sanitizer')

	if gloves: current_user.gloves = gloves
	if cloth: current_user.cloth = cloth
	if surgical: current_user.surgical = surgical
	if sanitizer: current_user.sanitizer = sanitizer

	db.session.commit()

	return redirect(url_for('up.supplies'))
