import os
from entidades.Gera_Dicionario.geraDicionario import *
from entidades.Formatador.formata_html import *

# import http.server
# import socketserver
# import threading
import os

__all__ = ["generator"]

def pegaDicionario(caminho_arquivo: str, type: str):

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:

        conteudo = arquivo.read()
        dicionario = geraDicionario(conteudo, type)

    return dicionario

def pegaArquivos(caminho_pasta: str):
    
    lista = os.listdir(caminho_pasta)
    return lista

def generator(caminho_pasta: str):

    arquivos = pegaArquivos(caminho_pasta)
    dicionario = dict()

    for arq in arquivos:
        if arq[-3:] == ".py":
            dicionario[arq[:-3]] = pegaDicionario(caminho_pasta+'/'+arq, "modulo")
    if "home.txt" in arquivos:
        dicionario["home"] = pegaDicionario(caminho_pasta+'/'+"home.txt", "home")
    
    print(dicionario)
    
    formataHTML(dicionario, caminho_pasta)

