import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            self.zoo.get_ticket_price(-1)
            
    def test_teen_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_adult_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_senior_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

if __name__ == '__main__':
    unittest.main()