from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
from os import getcwd
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+getcwd()+"test.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)


@app.route("/")
def index():
    users = User.query.all()
    return render_template('index.html',users=users)

@app.route("/create/", methods = [ "POST" ])
def create():
    name = request.form["name"]
    surname = request.form["surname"]
    email = request.form["email"]
    user_temp = User(name=name,surname=surname,email=email)
    db.session.add(user_temp)
    db.session.commit()
    return redirect("/")