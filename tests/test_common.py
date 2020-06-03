import unittest
import functions.common as common
import math


# test class
class TestCommon(unittest.TestCase):


    def test_add(self):
        self.assertEqual(common.add(1, 1), 2)

    def test_factorial(self):
        self.assertEqual(common.factorial(6), math.factorial(6))
        self.assertEqual(common.factorial(0), math.factorial(0))        # Test input of 0
        self.assertEqual(common.factorial(345), math.factorial(345))    # Test large number





# Allows us to run the tests immediately when this file is run
if __name__ == '__main__':
    unittest.main()
