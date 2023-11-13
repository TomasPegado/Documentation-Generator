import unittest
import Gera_Dicionario as gd


class TestExtrairDescricaoProjeto(unittest.TestCase):
    def test_01_busca_descricao_ok_condicao_retorno(self):
        print("Caso de Teste 01 - Buscar descrição com sucesso")

        with open("/home/tomas/PUC/Modular/arquivoTeste.txt", 'r') as arquivo:
            conteudo = arquivo.read()

        dicionario = gd.geraDicionario(conteudo)

        retorno_esperado = dicionario['descrição']

        self.assertEqual(retorno_esperado, "Esse projeto foi feito para gerar um dicionario a partir de um arquivo")
    

class TestExtrairModulo(unittest.TestCase):
    def test_01_busca_modulo_ok_condicao_retorno(self):
        print("Caso de Teste 01 - Buscar Modulo com sucesso")

        with open("/home/tomas/PUC/Modular/arquivoTeste.txt", 'r') as arquivo:
            conteudo = arquivo.read()

        dicionario = gd.geraDicionario(conteudo)

        retorno_esperado = dicionario['modulos']

        self.assertEqual(retorno_esperado, {"Gera_Dicionario": {}, "Documentacao": {}})

if __name__ == '__main__':
    unittest.main()


