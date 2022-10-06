from flask import Flask

app = Flask(__name__)

'''

funcao que soma dois elementos

'''

def soma(termo1,termo2):

    return termo1+termo2


'''

funcao raiz da minha aplicacao web

'''

@app.route("/")
def hello():

    return "<h1>Teste de segurança</h1>"

