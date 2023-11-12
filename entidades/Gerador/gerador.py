
import entidades.dicionario.Gera_Dicionario as gd

__all__ = ["pegaDicionario"]

def pegaDicionario(caminho_arquivo):

    with open(caminho_arquivo, 'r') as arquivo:

        conteudo = arquivo.read()
        dicionario = gd.geraDicionario(conteudo)

    return dicionario