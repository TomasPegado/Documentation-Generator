import regex as re

__all__ = ["geraDicionario"]

def geraDicionario(conteudo):
    
    dicionario = {
        'descrição': '', 
        'nome': '', 
        'imports': [],
        'funcoes': {}}
    buscaDescricaoDoModulo(conteudo, dicionario)
    buscaNome(conteudo, dicionario) 
    buscaImports(conteudo, dicionario)
    # buscaModulos(conteudo, dicionario)

    return dicionario

def buscaDescricaoDoModulo(conteudo, dicionario):

    # Definir o padrão de regex
    padrao = r'Descrição do Modulo:(.*?)"""'

    # Buscar pela descrição do modulo
    match = re.search(padrao, conteudo, re.DOTALL)

    if match:
        match = match.group(1).strip()  # Retorna o texto capturado, removendo espaços extras
        dicionario['descrição'] = match
        return match
    else:
        return "Descrição do modulo não encontrada."

def buscaNome(conteudo, dicionario):
    # Definir o padrão de regex
    padrao = r'Nome:(.*?)"""'

    # Buscar pela descrição do modulo
    match = re.search(padrao, conteudo, re.DOTALL)

    if match:
        match = match.group(1).strip()  # Retorna o texto capturado, removendo espaços extras
        dicionario['nome'] = match
        return match
    else:
        return "Nome do modulo não encontrada."

def buscaImports(conteudo, dicionario):

    # Definir o padrão de regex
    padrao1 = r'^import\s+([^\n]+)'
    padrao2 = r'from\s+([^\s]+)\s+import\s+'

    # Encontrar todas as correspondências para 'import'
    matches1 = re.findall(padrao1, conteudo, re.MULTILINE)
    matches2 = re.findall(padrao2, conteudo, re.MULTILINE)
    if matches1:
        dicionario['imports'] = matches1
    if matches2:
        dicionario['imports'] += matches2
    print(dicionario['imports'])
    return 

def buscaModulos(conteudo, dicionario):

    # Definir o padrão de regex
    padrao = r'Modulo:(.*?)"""'

    # Buscar pelo modulo
    match = re.search(padrao, conteudo, re.DOTALL)

    if match:
        match = match.group(1).strip()  # Retorna o texto capturado, removendo espaços extras
        dicionario['modulos'][match] = dict()

        # Buscar imports dentro do modulo
        padraoModulo = rf"Modulo:(.*?)Modulo:"
        conteudoModulo = re.search(padraoModulo, conteudo, re.DOTALL)
        conteudoModulo = conteudoModulo.group(1).strip()
        # print(conteudoModulo)
        matches = buscaImports(conteudoModulo)
        dicionario['modulos'][match]['imports'] = matches


        proximo = rf"{match}(.*)$" # Busca o modulo seguinte
        conteudo_restante = re.search(proximo, conteudo, re.DOTALL)
        conteudo_restante = conteudo_restante.group(1)
        proximoModulo = re.search(padrao, conteudo_restante, re.DOTALL)
        print(proximoModulo)

        try:
            capturado = proximoModulo.group(1) # Obtém a parte capturada pelo (.*)
            print(capturado)
            return buscaModulos(capturado, dicionario)
        
        except AttributeError:
            print("Nenhum conteudo restante.")
            return "Nenhum conteudo restante."
    else:
        return "Nenhum modulo foi encontrado."