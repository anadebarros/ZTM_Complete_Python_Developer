import section_15_199_testing
import unittest


class TestingRandom(unittest.TestCase):
    def test_guess_number(self):
        result = section_15_199_testing.guess_number(5, 5)
        self.assertTrue(result)

    def test_guess_number_wrong_guess(self):
        result = section_15_199_testing.guess_number(1, 5)
        self.assertFalse(result)

    def test_guess_number_wrong_number(self):
        result = section_15_199_testing.guess_number(11, 5)
        self.assertFalse(result)

    def test_guess_number_wrong_input(self):
        result = section_15_199_testing.guess_number("5", 9)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
