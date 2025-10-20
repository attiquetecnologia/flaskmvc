from flask import Blueprint, request, redirect, url_for, render_template, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_required

from database import db
from models import User

bp = Blueprint(__name__, "Auth")

@bp.route("/settings")
@login_required
def settings():
    pass

@bp.route("/login", methods=('POST', 'GET'))
def login():
    if "POST" in request.method:
        #lógica de login
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
    else:
        flash('Usuário ou senha inválidos')

    return render_template("auth/login.html")

def create_user(password: str):
    user = User(username="admin", nome="Administrador", password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()

    print(f"Criando usuário {user.as_dict()}")

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(somewhere)