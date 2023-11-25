from jinja2 import Template
import shutil
import os

__all__ = ['formataHTML']

def formataHTML(dados: dict, caminho: str):

    indice = criaIndice(dados)

    for arq in dados.keys():
        if arq == "home":
            formataHomePage(dados["home"], caminho, indice)
        else:
            formataModulePage(dados[arq], caminho, indice)

    criaAssetsCSS(caminho)        
    return

def criaIndice(dados: dict):
    
    lista_paginas = []
    for arq in dados.keys():

        dicionario = dict()
        dicionario['nome'] = arq
        dicionario['url'] = f'http://localhost:8000/{arq}.html'

        lista_paginas.append(dicionario)

    return lista_paginas

def criaAssetsCSS(caminho: str):

    # Caminho para o novo diretório
    pasta_assets = f'{caminho}/assets'

    # Caminho do arquivo CSS original
    arquivo_css_original = "entidades/formatador/paginas/assets/styles.css"

    # Caminho completo do arquivo no diretório de destino
    arquivo_css_destino = os.path.join(pasta_assets, os.path.basename(arquivo_css_original))

    # Verificar se o diretório já existe
    if not os.path.exists(pasta_assets):
        # Criar o diretório
        os.makedirs(pasta_assets)
        print(f"Diretório '{pasta_assets}' foi criado com sucesso.")
    else:
        print("O diretório já existe.")
    
    # Verificar se o arquivo original existe
    if os.path.exists(arquivo_css_original):

        # Copiar o arquivo
        shutil.copy(arquivo_css_original, arquivo_css_destino)
        print(f"Arquivo '{arquivo_css_original}' copiado para '{arquivo_css_destino}'")
    else:
        print("Arquivo CSS original não encontrado.")
    

def formataHomePage(dados: dict, caminho: str, indice: list):

    dados["modulos_projeto"] = indice

    # Carregar o template
    with open('entidades/formatador/paginas/template_home.html', 'r') as file:
        template = Template(file.read())

    # Renderizar o template com os dados
    html = template.render(dados)

    # Salvar o HTML gerado
    with open(f'{caminho}/home.html', 'w') as file:
        file.write(html)  

def formataModulePage(dados: dict, caminho: str, indice: list):

    pass



