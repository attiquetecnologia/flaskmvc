# Flask MVC

Usado para ensnino da arquitetura MVC...

**Instalação**

1 - Faça o clone do repositório para seu diretório de trabalho
$ git clone https://github.com/attiquetecnologia/flaskmvc.git

2- Acesse o diretório clonado flaskmvc
$ cd flaskmvc

3 - Crie e ative um virtualenv
**No Windows**
$ python -m venv .venv
$ python -m pip install --upgrade pip
$ . .venv/scripts/activate

**No Linux**
$ python3 -m venv .venv
$ python3 -m pip install --upgrade pip
$ source .venv/bin/activate

4 - Instale os pacotes
$ pip install -r requirements.txt

5- Crie o banco de dados
$ flask init-db

6- Adicione um usuário administrador
$ flask create-admin-user

7- Teste o aplicativo
http://127.0.0.1:5000


**Software para operação de dados**
SQLite Studio: somente sqlite, a versão portátil não precisa instalar: https://sqlitestudio.pl/

DBEaver: conecta em qualquer banco de dados, precisa de instalção e é multiplataforma: https://dbeaver.io/


**Software para design de banco**
https://www.drawio.com/