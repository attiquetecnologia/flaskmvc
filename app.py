"""

DOCUMENTAÇÃO DO FLASK LOGIN
https://flask-login.readthedocs.io/en/latest/
"""

import click
from flask import Flask, redirect, render_template, request, flash, session, url_for
from flask.cli import with_appcontext
from flask_login import LoginManager
from werkzeug.security import check_password_hash

from flask_migrate import Migrate


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
    app.cli.add_command(create_admin_user)
    
    migrate = Migrate(app, db)

    @login_manager.user_loader
    def load_user(user_id: int):      
        return User.get(user_id)

    @app.route("/") # cria uma rota
    def index(): # função que gerencia rota
        """ Página inicial"""
        if 'user' not in session:
            return redirect(url_for("auth.login"))
        
        return render_template("index.html") # Renderiza um template
    

    @app.route("/produtos")
    def produtos():
        return ""
    
    @app.route("/cadastro_exemplo", methods=('POST', 'GET'))
    def cadastro_exemplo():
        if request.method == 'POST':
            # Capturar dados do formulário para a classe instanciada
            from models import CamposExemplo
            camposExemplo = CamposExemplo(
                campo_texto = request.form.get("campo_texto")
                ,campo_texto_limitado = request.form.get("campo_texto_limitado") # até 10 caracteres
                ,campo_email = request.form.get("campo_email")
                ,campo_numero = request.form.get("campo_numero")
                ,campo_data = request.form.get("campo_data") # precisa fazer cast
                ,campo_selecao = request.form.get("campo_selecao")

                # Nos campos de checagem é preciso fazer uma validação para assumir verdadeiro ou falso
                ,chk_habilitado = "chk_habilitado" in request.form
                ,chk_desabilitado = "chk_desabilitado" in request.form # se estiver no dicináiro é True
                ,rb_resposta = request.form.get("rb_resposta") # Semelhante ao select box
                ,area_texto = request.form.get("area_texto")
            ) # fim instancia

            # iniciar uma sessão com banco para salvar os dados
            # e fazer o commit
            db.session.add(camposExemplo)
            db.session.commit()

            flash("Dados salvos com sucesso!!")
            
        return render_template('cadastro_exemplo.html')

    @app.route("/exclusao")
    def exclui_produto():
        return ""
    
    ## Registre módulos do sistema (bluprints controllers)
    # from arquivo import bp
    # app.register_blueprint(bp)

    from auth import bp # Autenticação
    app.register_blueprint(bp)

    return app # retorna o app criado

def init_db():
    db.drop_all()
    db.create_all()
    # db.reflect()

@click.command("create-admin-user")
@with_appcontext
def create_admin_user():
    from getpass import getpass
    from auth import create_user

    create_user(getpass("Digite a senha para admin: "))

@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    
    init_db()
    click.echo("Initialized the database.")

if __name__ == "__main__": # 'função principal' do python
    create_app().run(debug=True, host="0.0.0.0") # executa o flask na porta http://127.0.0.1:5000
