import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassa= Kassapaate()
        

    def test_kassan_saldo_ja_myynnit_alussa_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset+self.kassa.maukkaat, 0)

    def test_kateisosto_toimii(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(260), 20)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(420), 20)
        self.assertEqual(self.kassa.kassassa_rahaa, 100640)

    def test_kateisella_ostettujen_lounaiden_maara_kasvaa(self):
        self.kassa.syo_edullisesti_kateisella(260)
        self.assertEqual(self.kassa.edulliset, 1)
        self.kassa.syo_maukkaasti_kateisella(440)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_maksu_ei_riittava(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(190), 190)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(390), 390)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_korttiosto_toimii(self):
        self.kortti=Maksukortti(1000)
        self.assertTrue(self.kassa.syo_edullisesti_kortilla(self.kortti))
        self.assertEqual(self.kortti.saldo, 1000-240)
        self.assertTrue(self.kassa.syo_maukkaasti_kortilla(self.kortti))
        self.assertEqual(self.kortti.saldo, 1000-240-400)

    def test_kortilla_ostettujen_lounaiden_maara_kasvaa(self):
        self.kortti=Maksukortti(1000)
        self.assertTrue(self.kassa.syo_edullisesti_kortilla(self.kortti))
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertTrue(self.kassa.syo_maukkaasti_kortilla(self.kortti))
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_korttiosto_ei_toimi(self):
        self.kortti=Maksukortti(100)
        self.assertFalse(self.kassa.syo_edullisesti_kortilla(self.kortti))
        self.assertEqual(self.kortti.saldo,100)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertFalse(self.kassa.syo_maukkaasti_kortilla(self.kortti))
        self.assertEqual(self.kortti.saldo, 100)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kortilla_ostaessa_kassa_ei_kasva(self):
        self.kortti=Maksukortti(1000)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortille_rahaa_ladattaessa_kassan_rahamaara_kasvaa(self):
        self.kortti=Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(self.kortti, 400)
        self.assertEqual(self.kortti.saldo, 400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.kassa.lataa_rahaa_kortille(self.kortti, -400)
        self.assertEqual(self.kortti.saldo, 400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)