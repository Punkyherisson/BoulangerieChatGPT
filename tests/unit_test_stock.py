import unittest

from stock import verifier_stock, consommer_ingredients
from produits_pains import pains_classiques

class TestStock(unittest.TestCase):

    def setUp(self):
        self.stock_test = {
            "farine": 1000,
            "eau": 1000,
            "levure": 100,
            "sel": 50
        }

    def test_verifier_stock_suffisant(self):
        result = verifier_stock(self.stock_test, pains_classiques["Baguette"], 5)
        self.assertTrue(result)

    def test_verifier_stock_insuffisant(self):
        result = verifier_stock(self.stock_test, pains_classiques["Baguette"], 50)
        self.assertFalse(result)

    def test_consommation_stock(self):
        consommer_ingredients(self.stock_test, pains_classiques["Baguette"], 2)
        self.assertLess(self.stock_test["farine"], 1000)

if __name__ == "__main__":
    unittest.main()