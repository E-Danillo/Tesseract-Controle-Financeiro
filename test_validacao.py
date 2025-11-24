
mport unittest
from validacao import validar_valor, validar_descricao

class TestValidacao(unittest.TestCase):

    def test_valor_valido(self):
        ok, resultado = validar_valor("50")
        self.assertTrue(ok)
        self.assertEqual(resultado, 50.0)

    def test_valor_invalido_texto(self):
        ok, msg = validar_valor("abc")
        self.assertFalse(ok)

    def test_valor_zero(self):
        ok, msg = validar_valor("0")
        self.assertFalse(ok)

    def test_descricao_valida(self):
        ok, desc = validar_descricao("lanche")
        self.assertTrue(ok)
        self.assertEqual(desc, "lanche")

    def test_descricao_numero(self):
        ok, msg = validar_descricao(123)
        self.assertFalse(ok)

if __name__ == "__main__":
    unittest.main()