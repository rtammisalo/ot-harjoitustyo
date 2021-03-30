import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(10000)
    
    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_luotu_kassapaate_sisaltaa_1000euroa_ja_0_myytya_lounasta(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateiseilla_ostettu_lounas_kasvattaa_kassapaatteen_saldoa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100480)

        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100880)
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101280)

    def test_kateisella_ostettu_lounas_kasvattaa_kassapaatteen_myynteja(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.edulliset, 2)

        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.maukkaat, 2)

    def test_kateisella_ostettu_lounas_antaa_takaisin_vaihtorahat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450), 50)

    def test_kateisostossa_kassapaate_ei_hyvaksy_liian_pienta_maksua_ja_rahat_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(10), 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(10), 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortilla_ostettu_lounas_ei_kasvata_kassapaatteen_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortilla_ostettu_lounas_veloitetaan_kortilta(self):
        kortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(kortti.saldo, 0)
        self.assertEqual(self.kortti.saldo, 9760)

        kortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(kortti.saldo, 0)
        self.assertEqual(self.kortti.saldo, 9360)

    def test_kortilla_onnistuneesti_ostettu_lounas_palauttaa_true(self):
        kortti = Maksukortti(240)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(kortti))
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.kortti))

        kortti = Maksukortti(400)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(kortti))
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.kortti))

    def test_kortilla_ostettu_lounas_kasvattaa_kassapaatteen_myynteja(self):
        kortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 2)
        
        kortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 2)

    def test_korttiosto_palauttaa_false_jos_kortilla_ei_ole_tarpeeksi_rahaa(self):
        kortti = Maksukortti(10)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(kortti))
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(kortti))

    def test_korttiosto_epaonnistuessaan_ei_kasvata_myytyja_lounaita(self):
        kortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_epaonnistuessaan_ei_muuta_kortin_saldoa(self):
        kortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 10)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 10)

    def test_korttiosto_epaonnistuessaan_ei_muuta_kassan_saldoa(self):
        kortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttille_rahan_lataaminen_kasvattaa_kassan_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
    
    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_rahan_lataaminen_kasvattaa_kortin_saldoa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kortti.saldo, 10100)