
import unittest
from Lista_Generica import insereElemento, removeElemento, buscaElemento, insereChave

class TestListaGenerica(unittest.TestCase):
    def setUp(self):
        # Inicializa um dicionário de teste para cada método
        self.dicionario = {
            'numeros': [1, 2, 3],
            'letras': ['a', 'b', 'c']
        }

    def test_insereElemento(self):
        # Testa a inserção de um elemento em uma chave existente
        insereElemento(self.dicionario, 4, 'numeros')
        self.assertIn(4, self.dicionario['numeros'])
        
        # Testa a inserção de um elemento em uma nova chave
        insereElemento(self.dicionario, 'd', 'nova_chave')
        self.assertIn('d', self.dicionario['nova_chave'])

    def test_removeElemento(self):
        # Testa a remoção de um elemento
        removeElemento(self.dicionario, 2, 'numeros')
        self.assertNotIn(2, self.dicionario['numeros'])

    def test_buscaElemento(self):
        # Testa a busca por um elemento
        self.assertTrue(buscaElemento(3, None, 'numeros', self.dicionario))
        self.assertFalse(buscaElemento(4, None, 'numeros', self.dicionario))

    def test_insereChave(self):
        # Testa a inserção de uma nova chave
        insereChave(self.dicionario, 'simbolos')
        self.assertIn('simbolos', self.dicionario)
        self.assertEqual(self.dicionario['simbolos'], [])

if __name__ == '__main__':
    unittest.main()
