from inventar import *
import unittest
import collections


class TestInventar(unittest.TestCase):

    def assertDictCounterEqual(self, first, second, msg=None):
        def dict_counter(d):
            d_copy = dict(d)
            for k, v in d_copy.items():
                d_copy[k] = collections.Counter(v)
            return d_copy
        self.assertDictEqual(dict_counter(first), dict_counter(second), msg)

    def test_zaloga(self):
        inv = {"kruh": 5, "kajzerica": 4, "makovka": 3}
        self.assertEqual(zaloga(inv, "kruh"), 5)
        self.assertEqual(zaloga(inv, "kajzerica"), 4)
        self.assertEqual(zaloga(inv, "makovka"), 3)

    def test_prodaj(self):
        inv = {"kruh": 5, "kajzerica": 4, "makovka": 3}
        self.assertIsNone(prodaj(inv, "kajzerica", 2), "Funkcija naj ne vrača ničesar!")
        self.assertEqual(zaloga(inv, "kruh"), 5)
        self.assertEqual(zaloga(inv, "kajzerica"), 2)
        self.assertEqual(zaloga(inv, "makovka"), 3)

        prodaj(inv, "kruh", 5)
        self.assertTrue("kruh" not in inv or (zaloga(inv, "kruh"), 0))
        self.assertEqual(zaloga(inv, "kajzerica"), 2)
        self.assertEqual(zaloga(inv, "makovka"), 3)

    def test_primanjkljaj(self):
        inventar = {
            'sir': 8, 'kruh': 15, 'makovka': 10, 'pasja radost': 2,
            'pašteta': 10, 'mortadela': 4, 'klobasa': 7
        }
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 10}),
            {})
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 12}),
            {"makovka": 2})
        self.assertDictEqual(
            primanjkljaj(inventar, {"kruh": 2, "makovka": 12, "pivo": 3}),
            {"makovka": 2, "pivo": 3})
        self.assertDictEqual(primanjkljaj(inventar, {}), {})
        self.assertDictEqual(primanjkljaj(inventar, inventar), {})


if __name__ == '__main__':
    unittest.main(verbosity=2)
