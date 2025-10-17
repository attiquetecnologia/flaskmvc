"""
Esse arquivo é um exemplo de controller
"""

from flask import Blueprint, request, redirect, url_for, render_template, flash
from werkzeug.security import check_password_hash, generate_password_hash

from database import db
from models import User

"""
    ControllerExemplo: Nome da blueprint que será usada em urlfor
        Ex: url_for('ControllerExemplo.nome_funcao')
            url_for('ProdutosController.cadastrar')

    url_prefix: Prefixo de URL usado nas urls como em, 
        deixe em branco caso queira usar a raiz do site
        https://127.0.0.1:5000/url_prefix/cadastrar
        https://127.0.0.1:5000/url_prefix/listar

"""
bp = Blueprint(__name__, "ControllerExemplo", url_prefix="/exemplos")

# https://127.0.0.1:5000/url_prefix/listar
# https://127.0.0.1:5000/produtos/listar -> se url_prefix = 'produtos'
# https://127.0.0.1:5000/listar -> se url_prefix = None
@bp.route("/listar")
def listar():
    """
    Lista os dados da tabela CadastroExemplo
    """
    return ""

@bp.route("/cadastro_exemplo", methods=('POST', 'GET'))
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

@bp.route("/exclusao")
def exclui_produto():
    return ""