import unittest
import entidades.Gerador.gerador as ge

class TestExtraiConteudoDaPasta(unittest.TestCase):

    def test_01_extrai_arquivos_python(self):
        print("Caso de Teste 01 - Buscar arquivos com sucesso")

        caminho = "/home/tomas/PUC/Modular/modulos"

        retorno_esperado = ge.pegaArquivos(caminho)

        self.assertEqual(retorno_esperado, ["Lista_Generica.py", "Gera_Dicionario.py"])

class TestGeraDicionario(unittest.TestCase):

    def test_02_gera_dicionario_dados(self):
        print("Caso de Teste 02 - Gerar Dicionario com todos os dados com sucesso")

        caminho = "/home/tomas/PUC/Modular/modulos"

        retorno_esperado = ge.generator(caminho)

        dicionario = {'Lista_Generica': {'descrição': '', 'nome': '', 'imports': [], 'funcoes': {'insereElemento': {}, 'removeElemento': {}, 'buscaElemento': {}, 'insereChave': {}}, '_all_': []}, 'Gera_Dicionario': {'descrição': 'Esse projeto foi feito para gerar um dicionario a partir de um arquivo', 'nome': 'Gera_Dicionario', 'imports': ['regex as re'], 'funcoes': {'geraDicionario': {'descricao': 'Aqui esta a descrição da função geraDicionario\n\n    Parameters\n    ----------\n    conteudo : _type_\n        _description_\n\n    Returns\n    -------\n    _type_\n        _description_'}, 'buscaDescricaoDoModulo': {'descricao': 'Aqui esta a descrição da função geraDicionario\n\n    Parameters\n    ----------\n    conteudo : str\n        _description_\n    dicionario : dict\n        _description_\n\n    Returns\n    -------\n    _type_\n        _description_'}, 'buscaNome': {'descricao': '_summary_\n\n    Parameters\n    ----------\n    conteudo : str\n        _description_\n    dicionario : dict\n        _description_\n\n    Returns\n    -------\n    _type_\n        _description_'}, 'buscaImports': {'descricao': '_summary_\n\n    Parameters\n    ----------\n    conteudo : str\n        _description_\n    dicionario : dict\n        _description_'}, 'buscaDescricaoFuncao': {'descricao': '_summary_\n\n    Parameters\n    ----------\n    conteudo : str\n        _description_\n    dicionario : dict\n        _description_\n    funcao : str\n        _description_'}, 'buscaFuncoes': {'descricao': '_summary_\n\n    Parameters\n    ----------\n    conteudo : str\n        _description_\n    dicionario : dict\n        _description_'}, 'buscaAll': {'descricao': '_summary_\n\n    Parameters\n    ----------\n    conteudo : str\n        _description_\n    dicionario : dict\n        _description_'}}, '_all_': ['geraDicionario']}}

        self.assertEqual(retorno_esperado, dicionario)


if __name__ == '__main__':
    unittest.main()