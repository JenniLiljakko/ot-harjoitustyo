import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual("saldo: 0.1", str(self.maksukortti))

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual("saldo: 0.2", str(self.maksukortti))

    def test_rahan_ottaminen_toimii_oikein(self):
        self.assertTrue(self.maksukortti.ota_rahaa(5))
        self.assertEqual("saldo: 0.05", str(self.maksukortti))
    
    def test_saldo_ei_vahene_jos_rahaa_ei_ole_tarpeeksi(self):
        self.assertFalse(self.maksukortti.ota_rahaa(15))
        self.assertEqual("saldo: 0.1", str(self.maksukortti))
        