import os
from entidades.Gera_Dicionario.geraDicionario import *
from entidades.Formatador.formata_html import *

# import http.server
# import socketserver
# import threading
import os

__all__ = ["generator"]

def pegaDicionario(caminho_arquivo: str, type: str):

    with open(caminho_arquivo, 'r') as arquivo:

        conteudo = arquivo.read()
        dicionario = geraDicionario(conteudo, type)

    return dicionario

def pegaArquivos(caminho_pasta: str):
    
    lista = os.listdir(caminho_pasta)
    return lista

def iniciaLocalServer(caminho_pasta: str): 

    # print("diretorio atual", os.getcwd())
    # os.chdir(caminho_pasta)

    # PORT = 8000
    # Handler = http.server.SimpleHTTPRequestHandler
    # print("diretorio atual", os.getcwd())

    # def start_server():
    #     with socketserver.TCPServer(("", PORT), Handler) as httpd:
    #         httpd.allow_reuse_address = True
    #         print(f"Servidor iniciado em http://localhost:{PORT}/home.html")
    #         print("Abra esta URL no navegador de sua escolha.")
    #         httpd.serve_forever()

    # # Iniciar o servidor em uma thread separada
    # thread = threading.Thread(target=start_server)
    # thread.daemon = True
    # thread.start()
    pass

def generator(caminho_pasta: str):

    arquivos = pegaArquivos(caminho_pasta)
    dicionario = dict()

    for arq in arquivos:
        if arq[-3:] == ".py":
            dicionario[arq[:-3]] = pegaDicionario(caminho_pasta+'/'+arq, "modulo")
    if "home.txt" in arquivos:
        dicionario["home"] = pegaDicionario(caminho_pasta+'/'+"home.txt", "home")
    
    formataHTML(dicionario, caminho_pasta)
    
    print("Iniciar Local Host")
    iniciaLocalServer(caminho_pasta)

