import unittest
from cryptography import rot13


class CryptoTests(unittest.TestCase):
    def test_single_lower_case(self):
        self.assertEqual(rot13("a"), "n")
        self.assertEqual(rot13("b"), "o")
        self.assertEqual(rot13("c"), "p")

    def test_single_lower_case_wrap(self):
        self.assertEqual(rot13("x"), "k")
        self.assertEqual(rot13("y"), "l")
        self.assertEqual(rot13("z"), "m")


if __name__ == "__main__":
    unittest.main()
