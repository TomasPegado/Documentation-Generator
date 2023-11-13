import regex as re

__all__ = ["geraDicionario"]

def geraDicionario(conteudo):
    
    dicionario = {'descrição': '', 'modulos': {}}
    buscaDescricaoDoProjeto(conteudo, dicionario)
    buscaModulos(conteudo, dicionario)

    return dicionario

def buscaDescricaoDoProjeto(conteudo, dicionario):

    # Definir o padrão de regex
    padrao = r'Descrição do Projeto:(.*?)"""'

    # Buscar pela descrição do projeto
    match = re.search(padrao, conteudo, re.DOTALL)

    if match:
        match = match.group(1).strip()  # Retorna o texto capturado, removendo espaços extras
        dicionario['descrição'] = match
        return match
    else:
        return "Descrição do projeto não encontrada."

def buscaImports(conteudo):

    # Definir o padrão de regex
    padrao = r'^import\s+([^\n]+)'

    # Encontrar todas as correspondências para 'import'
    matches = re.findall(padrao, conteudo, re.MULTILINE)
    print(matches)

    return matches

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