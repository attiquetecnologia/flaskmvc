"""

DOCUMENTAÇÃO DO FLASK LOGIN
https://flask-login.readthedocs.io/en/latest/
"""

import click
from flask import Flask, redirect, render_template, request, flash, session, url_for
from flask.cli import with_appcontext
from flask_login import LoginManager
from werkzeug.security import check_password_hash

from database import db
from models import User

def create_app(): # cria uma função para definir o aplicativo
    app = Flask(__name__) # instancia o Flask
    app.secret_key = "abax"

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager = LoginManager()   
    login_manager.init_app(app)

    db.init_app(app)
    app.cli.add_command(init_db_command)

    @login_manager.user_loader
    def load_user(user_id: int):      
        return User.get(user_id)

    @app.route("/") # cria uma rota
    def index(): # função que gerencia rota
        """ Página inicial"""
        if 'user' not in session:
            return redirect(url_for("login"))
        
        return render_template("index.html") # Renderiza um template

    @app.route("/login", methods=('POST', 'GET'))
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

        return render_template("login.html")
    

    @app.route("/produtos") 
    def produtos():
        return ""
    
    @app.route("/cadastro")
    def cadastro_produto():
        return ""

    @app.route("/exclusao")
    def exclui_produto():
        return ""

    return app # retorna o app criado

def init_db():
    db.drop_all()
    db.create_all()
    # db.reflect()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    
    init_db()
    click.echo("Initialized the database.")

if __name__ == "__main__": # 'função principal' do python
    create_app().run(debug=True, host="0.0.0.0") # executa o flask na porta http://127.0.0.1:5000
