from flask import Flask

app = Flask(__name__)

def soma(a,b):
    return a+b


# funcao raiz do meu projeto
@app.route("/")
def hello():
    return "<h1>Teste de segurança</h1>"

