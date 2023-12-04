from jinja2 import Template
import shutil
import os

__all__ = ['formataHTML']

def formataHTML(dados: dict, caminho: str):

    criaStatic(caminho)
    
    # Imprime as chaves do dicionário 'dados' para verificar se há duplicatas
    print("Dados.keys() antes de criar o índice:", dados.keys())
    
    # Cria um índice dos dados, o qual é utilizado para gerar links nas páginas HTML
    indice = criaIndice(dados)

    print("Dados before HTML formatting:", dados)
    
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

    # Verificar se o diretório já existe
    if not os.path.exists(f'{caminho}/static'):
        # Criar o diretório
        os.makedirs(f'{caminho}/static')
        print(f"Diretório '{f'{caminho}/static'}' foi criado com sucesso.")
    else:
        print("O diretório static já existe.")

def criaIndice(dados: dict):
    
    lista_paginas = []
    for arq in dados.keys():
        dicionario = dict()
        dicionario['nome'] = arq
        dicionario['url'] = f'http://localhost:8000/static/{arq}.html'
        lista_paginas.append(dicionario)
    
    # Imprime a lista completa de páginas após criar todas as entradas
    print("Índice criado:", lista_paginas)

    return lista_paginas


def criaAssetsCSS(caminho: str):

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
        print("O diretório já existe.")
    
    # Verificar se o arquivo original existe
    if os.path.exists(arquivo_css_original):

        # Copiar o arquivo
        shutil.copy(arquivo_css_original, arquivo_css_destino)
        print(f"Arquivo '{arquivo_css_original}' copiado para '{arquivo_css_destino}'")
    else:
        print("Arquivo CSS original não encontrado.")
        
def nl2br(value):
    """Converts newlines in a string to <br> tags for HTML display."""
    return value.replace("\n", "<br>\n") if value else ''

def formataHomePage(dados: dict, caminho: str, indice: list):

    dados["modulos_projeto"] = indice
    
    print("Home page data:", dados)

    # Carregar o template
    with open('entidades/Formatador/paginas/template_home.html', 'r', encoding='utf-8') as file:
        template = Template(file.read())

    # Renderizar o template com os dados
    html = template.render(dados)

    # Salvar o HTML gerado
    with open(f'{caminho}/static/home.html', 'w', encoding="utf-8") as file:
        file.write(html)  

def formataModulePage(dados: dict, caminho: str, indice: list):

    dados["modulos_projeto"] = indice

    # Carregar o template para a página do módulo
    with open('entidades/Formatador/paginas/template_modulo.html', 'r', encoding='utf-8') as file:
        template = Template(file.read())
        
    print(f"Module page data for {dados['nome']}:", dados)
    
    for funcao, detalhes in dados['funcoes'].items():
        detalhes['descricao'] = detalhes['descricao'].replace('\n\n', '</p><p>').replace('\n', '<br>')

    # Renderizar o template com os dados do módulo
    html = template.render(dados)

    # Salvar o HTML gerado para o módulo específico
    with open(f'{caminho}/static/{dados["nome"]}.html', 'w', encoding="utf-8") as file:
        file.write(html)




