"""
Descrição do Módulo:
Esse módulo foi feito para criar e formatar os arquivos html da documentação
usando o dicionario que contem os dados dos módulos
    
"""
"""
Nome: formata_html
"""

from jinja2 import Template
import shutil
import os

__all__ = ['formataHTML']

def formataHTML(dados: dict, caminho: str):
    """
    Principal função do módulo. Ela recebe os dados e cria os arquivos.
    
    Parâmetros:
    - dados (dict): O dicionário onde os dados dos modulos estão.
    - caminho: O caminho do diretório onde os arquivos devem ser criados
    """

    criaStatic(caminho)
    
    # Imprime as chaves do dicionário 'dados' para verificar se há duplicatas
    # print("Dados.keys() antes de criar o índice:", dados.keys())
    
    # Cria um índice dos dados, o qual é utilizado para gerar links nas páginas HTML
    indice = criaIndice(dados)

    # print("Dados before HTML formatting:", dados)
    
    # Itera sobre os dados para formatar as páginas HTML corretamente
    for arq in dados.keys():
        if arq == "home":
            formataHomePage(dados["home"], caminho, indice)
        else:
            formataModulePage(dados[arq], caminho, indice)

    # Cria os assets CSS necessários para as páginas HTML
    criaAssetsCSS(caminho)        
    return


def criaStatic(caminho: str):
    """
    Função que verifica se existem no caminho uma pasta static e,
    se não tiver, cria uma no local. Isso é necessário pois o servidor Flask
    procura os arquivos html em uma pasta static. Então, usamos essa pasta para
    alocar os arquivos html do projeto.
    
    Parâmetros:
    - caminho: O caminho do diretório onde os arquivos devem ser criados
    """

    # Verificar se o diretório já existe
    if not os.path.exists(f'{caminho}/static'):
        # Criar o diretório
        os.makedirs(f'{caminho}/static')
        print(f"Diretório '{f'{caminho}/static'}' foi criado com sucesso.")
    else:
        print("\nO diretório static já existe.")

def criaIndice(dados: dict):
    """
    Função para criar os links para cada página do programa e, assim, termos indices
    para navegação entre as páginas.
    
    Parâmetros:
    - dados (dict): O dicionário onde os dados dos modulos estão.
    """
    
    lista_paginas = []
    for arq in dados.keys():
        dicionario = dict()
        dicionario['nome'] = arq
        dicionario['url'] = f'http://localhost:8000/static/{arq}.html'
        lista_paginas.append(dicionario)
    
    # Imprime a lista completa de páginas após criar todas as entradas
    # print("Índice criado:", lista_paginas)

    return lista_paginas


def criaAssetsCSS(caminho: str):
    """
    Função para verificar a existencia e criar uma nova pasta assets, dentro da static
    para conter o arquivo css de formatação das páginas html.
    
    Parâmetros:
    - caminho: O caminho do diretório onde os arquivos devem ser criados
    """

    # Caminho para o novo diretório
    pasta_assets = f'{caminho}/static/assets'

    # Caminho do arquivo CSS original
    arquivo_css_original = "entidades/Formatador/paginas/assets/styles.css"

    # Caminho completo do arquivo no diretório de destino
    arquivo_css_destino = os.path.join(pasta_assets, os.path.basename(arquivo_css_original))

    # Verificar se o diretório já existe
    if not os.path.exists(pasta_assets):
        # Criar o diretório
        os.makedirs(pasta_assets)
        print(f"Diretório '{pasta_assets}' foi criado com sucesso.")
    else:
        print("O diretório static/assets já existe.\n")
    
    # Verificar se o arquivo original existe
    if os.path.exists(arquivo_css_original):

        # Copiar o arquivo
        shutil.copy(arquivo_css_original, arquivo_css_destino)
        print(f"Arquivo '{arquivo_css_original}' copiado para '{arquivo_css_destino}'\n")
    else:
        print("Arquivo CSS original não encontrado.")
        
def nl2br(value):
    """
    Converts newlines in a string to <br> tags for HTML display.
    
    Parâmetros:
    - value: 
    """
    return value.replace("\n", "<br>\n") if value else ''

def formataHomePage(dados: dict, caminho: str, indice: list):
    """
    Função que cria e formata a página home da documentação.
    
    Parâmetros:
    - dados (dict): O dicionário onde os dados dos modulos estão.
    - caminho: O caminho do diretório onde os arquivos devem ser criados
    - indice: lista dos indices com os links para navegação
    """
    

    dados["modulos_projeto"] = indice
    
    # print("Home page data:", dados)

    # Carregar o template
    with open('entidades/Formatador/paginas/template_home.html', 'r', encoding='utf-8') as file:
        template = Template(file.read())

    # Renderizar o template com os dados
    html = template.render(dados)

    # Salvar o HTML gerado
    with open(f'{caminho}/static/home.html', 'w', encoding="utf-8") as file:
        file.write(html)  

def formataModulePage(dados: dict, caminho: str, indice: list):
    """
    Função que cria e formata as páginas dos módulos da documentação.
    
    Parâmetros:
    - dados (dict): O dicionário onde os dados dos modulos estão.
    - caminho: O caminho do diretório onde os arquivos devem ser criados
    - indice: lista dos indices com os links para navegação
    """
    dados["modulos_projeto"] = indice

    # Carregar o template para a página do módulo
    with open('entidades/Formatador/paginas/template_modulo.html', 'r', encoding='utf-8') as file:
        template = Template(file.read())
        
    # print(f"Module page data for {dados['nome']}:", dados)

    # Esta parte é para garantir que a descrição seja uma string formatada corretamente para HTML
    for funcao, detalhes in dados['funcoes'].items():
        if isinstance(detalhes, dict) and 'descricao' in detalhes:
            detalhes['descricao'] = nl2br(detalhes['descricao'])

    # Renderizar o template com os dados do módulo
    html = template.render(dados)

    # Salvar o HTML gerado para o módulo específico
    with open(f'{caminho}/static/{dados["nome"]}.html', 'w', encoding="utf-8") as file:
        file.write(html)





