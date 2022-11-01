import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_neg_storage(self):
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_neg_saldo(self):
        self.varasto = Varasto(0, -1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_add_neg_storage(self):
        p = self.varasto.paljonko_mahtuu()
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(p, self.varasto.paljonko_mahtuu())

    def test_add_much(self):
        self.varasto.lisaa_varastoon(100000000)
        self.assertAlmostEqual(self.varasto.tilavuus, self.varasto.saldo)

        otet = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(otet, 0)

        saldo = self.varasto.saldo
        otet = self.varasto.ota_varastosta(1000000000)
        self.assertAlmostEqual(otet, saldo)
        self.assertAlmostEqual(self.varasto.saldo, 0)

        self.assertEqual(
            f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}", True)  # self.varasto.__str__())

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
