
from entidades.Gerenciador.gerenciador import *
from flask import Flask, redirect, url_for

caminho = input("\nInsira o caminho do arquivo contendo os modulos: ")

generator(caminho)

app = Flask(__name__, static_folder=caminho + '/static')

@app.route('/')
def home():
    return redirect(url_for('static', filename='home.html'))

if __name__ == '__main__':
    
    app.run(port=8000) 
