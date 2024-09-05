import unittest
import main as main

class TestDummy(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(main.subtract(5, 3), 2)

    def test_division(self):
        self.assertEqual(main.division(6, 2), 3)

    # def test_multiplication(self):
    #     self.assertEqual(main.multiplication(6, 2), 12)

        

if __name__ == '__main__':
    unittest.main()
