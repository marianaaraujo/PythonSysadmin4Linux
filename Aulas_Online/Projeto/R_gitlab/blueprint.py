from flask import Blueprint, render_template, redirect, url_for
import requests

gitlab_routes = Blueprint("gitlab", __name__, url_prefix='/gitlab')
token = 'abc123'

@gitlab_routes.route("")
def index():
	if not "logged" in session or not session["logged"]:
		redirect(url_for('index')) 
	try:
		usuarios = requests.get("http://192.168.0.100/api/v4/users?private_token=%s"%(token))
		usuarios = usuarios.json()
	except Exception as error:
		return "%s"%(error)
	return render_template("gitlab.html")