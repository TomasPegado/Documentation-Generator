from jinja2 import Template

__all__ = ['formataHTML']

def formataHTML(dados: dict, caminho: str):

    indice = criaIndice(dados, caminho)

    for arq in dados.keys():
        if arq == "home":
            formataHomePage(dados["home"], caminho, indice)
        else:
            formataModulePage(dados[arq], caminho, arq)        
    return

def criaIndice(dados: dict, caminho: str):
    
    lista_paginas = []
    for arq in dados.keys():
        dicionario = dict()
        dicionario['nome'] = arq
        dicionario['url'] = f'{caminho}/{arq}.html'
        lista_paginas.append(dicionario)
    return lista_paginas

def formataHomePage(dados: dict, caminho: str, indice: list):

    dados["modulos_projeto"] = indice    
    return

def formataModulePage(dados: dict, caminho: str, indice: list):

    return



