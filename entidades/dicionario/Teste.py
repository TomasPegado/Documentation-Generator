import unittest
# from entidades.dicionario import *
import Gera_Dicionario as gd


class TestExtrairDescricaoModulo(unittest.TestCase):
    def test_01_busca_descricao_ok_condicao_retorno(self):
        print("Caso de Teste 01 - Buscar com sucesso")

        with open("/home/tomas/PUC/Modular/arquivoTeste.txt", 'r') as arquivo:
            conteudo = arquivo.read()

        dicionario = gd.geraDicionario(conteudo)

        retorno_esperado = dicionario['descrição']

        self.assertEqual(retorno_esperado, "Esse módulo foi feito para gerar um dicionario a partir de um arquivo")

if __name__ == '__main__':
    unittest.main()


