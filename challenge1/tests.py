import unittest
from cryptography import rot13


class CryptoTests(unittest.TestCase):
    def test_single_lower_case(self):
        self.assertEqual(rot13("a"), "n")
        self.assertEqual(rot13("b"), "o")
        self.assertEqual(rot13("c"), "p")


if __name__ == "__main__":
    unittest.main()
