#Jonatan Rassekhnia
#2023.04.23
#Lab 6 Code Coverage
#Karlstad University

import unittest
from operations import compute


class TestApp(unittest.TestCase):
    def setUp(self):
        self.a = 25
        self.b = 0

    def test_subtraction(self):  # test suites case for subtraction
        result = compute(self.a, self.b, 'subtract')
        self.assertEqual(result, 5)

    def test_addition(self):  # test suites case for addition
        result = compute(self.a, self.b, 'add')
        self.assertEqual(result, 5)

    def test_multiplication(self):  # test suites case for multiplication
        result = compute(self.a, self.b, 'multiply')
        self.assertEqual(result, 5)

    def test_division(self):  # test case for division
        result = compute(self.a, self.b, 'divide')
        self.assertEqual(result, 5)

    def suite():
        suites = unittest.TestSuite()
        suites.addTests(
            unittest.TestLoader().loadTestsFromTestCase(TestApp)
        )
        return suites


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(TestApp.suite())

print("Jonatan Rassekhnia")
