
from entidades.dicionario.Gera_Dicionario import *

__all__ = ["pegaDicionario"]

def pegaDicionario(caminho_arquivo):

    with open(caminho_arquivo, 'r') as arquivo:

        conteudo = arquivo.read()
        dicionario = geraDicionario(conteudo)

    return dicionario