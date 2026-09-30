import unittest

from registro_voti import RegistroVoti


class TestRegistroVoti(unittest.TestCase):
    def test_media_calcola_la_media_di_tutti_i_voti(self):
        registro = RegistroVoti()
        registro.aggiungi_voto("Ada", 8)
        registro.aggiungi_voto("Ada", 10)
        registro.aggiungi_voto("Luca", 6)

        self.assertEqual(registro.media(), 8.0)


if __name__ == "__main__":
    unittest.main()