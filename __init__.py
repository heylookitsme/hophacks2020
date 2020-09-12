from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
	app = Flask(__name__)

	app.config['SECRET_KEY'] = '12345678'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

	db.init_app(app)

	login_manager = LoginManager()
	login_manager.login_view = 'um.login'
	login_manager.init_app(app)

	from user_management import um as umbp
	app.register_blueprint(umbp)

	from user_pages import up as upbp
	app.register_blueprint(upbp)

	@app.route('/projects/hophacks2020')
	def home():
		return render_template("index.html") 

	@app.errorhandler(404)
	def page_not_found(e):
		return render_template("404err.html")

	return app
