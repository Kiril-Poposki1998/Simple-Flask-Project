from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from markupsafe import escape
from os import getcwd

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+getcwd()+"test.db"
db = SQLAlchemy(app)


class Registration(Form):
    name = StringField("name", [validators.DataRequired()])
    surname = StringField("surname", [validators.DataRequired()])
    email = StringField("email", [validators.DataRequired()])


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)


@app.route("/")
def index():
    users = User.query.all()
    return render_template('index.html', users=users, form=None)


@app.route("/create_user/", methods=["POST"])
def create():
    form = Registration(request.form)
    name = request.form["name"]
    surname = request.form["surname"]
    email = request.form["email"]
    if request.method == "POST" and form.validate():
        user_temp = User(name=name, surname=surname, email=email)
        db.session.add(user_temp)
        db.session.commit()
    users = User.query.all()
    return render_template("index.html",users=users,form=form)