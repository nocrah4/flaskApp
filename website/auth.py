from flask import Blueprint,render_template

auth=Blueprint('auth', __name__)

@auth.route('/register')
def index():
    return render_template("register.html")



@auth.route('/medical-team')
def inner():
    return render_template("medical-team.html")

@auth.route('/health-info')
def healthinfo():
    return render_template("healthinfo.html")

@auth.route('/')
def home():
    return"<p>home</p>"
