# Flask MVC

Usado para ensnino da arquitetura MVC...

**Instalação**

1 - Faça o clone do repositório para seu diretório de trabalho
$ git clone https://github.com/attiquetecnologia/flaskmvc.git

2 - Crie e ative um virtualenv
**No Windows**
$ python -m venv .venv
$ python -m pip install --upgrade pip
$ . .venv/scripts/activate

**No Linux**
$ python3 -m venv .venv
$ python3 -m pip install --upgrade pip
$ source .venv/bin/activate

3 - Instale os pacotes
$ pip install -r requirements.txt

4- Crie o banco de dados
$ flask init-db

5- Adicione um usuário administrador
$ flask create-admin-user