from flask import Blueprint, request, redirect, url_for, render_template, flash
from werkzeug.security import check_password_hash


from models import User

bp = Blueprint(__name__, "Auth")
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