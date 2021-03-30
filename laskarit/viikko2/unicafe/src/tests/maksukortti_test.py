import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_asetetaan_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_positiivisen_summan_lataaminen_onnistuu(self):
        self.maksukortti.lataa_rahaa(90)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")
    
    def test_negatiivisen_summan_lataaminen_ei_onnistu(self):
        self.maksukortti.lataa_rahaa(-10)
        self.assertNotEqual(str(self.maksukortti), "saldo: 0.0")

    def test_kortilta_otto_vahentaa_saldoa(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
    
    def test_kortilta_otto_ei_muuta_saldoa_jos_saldo_ei_riita(self):
        self.maksukortti.ota_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_kortilta_otto_palauttaa_false_jos_saldo_ei_riita(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1000))

    def test_kortilta_otto_palauttaa_true_jos_saldo_riittaa(self):
        self.assertTrue(self.maksukortti.ota_rahaa(5))