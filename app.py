import click
from flask import Flask, redirect, render_template, request, jsonify, session, url_for
from flask.cli import with_appcontext
from database import db

def create_app(): # cria uma função para definir o aplicativo
    app = Flask(__name__) # instancia o Flask
    app.secret_key = "abax"

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    app.cli.add_command(init_db_command)

    @app.route("/") # cria uma rota
    def index(): # função que gerencia rota
        """ Página inicial"""
        if 'user' not in session:
            return redirect(url_for("login"))
        
        return render_template("index.html") # Renderiza um template

    @app.route("/login")
    def login():
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
