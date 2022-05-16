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

    def test_single_upper_case(self):
        self.assertEqual(rot13("D"), "Q")
        self.assertEqual(rot13("E"), "R")
        self.assertEqual(rot13("F"), "S")

    def test_single_upper_case_wrap(self):
        self.assertEqual(rot13("U"), "H")
        self.assertEqual(rot13("V"), "I")
        self.assertEqual(rot13("W"), "J")

    def test_lower_case_word(self):
        self.assertEqual(rot13("abcdefghijklmnopqrstuvwxyz"),
                         "nopqrstuvwxyzabcdefghijklm")

    def test_upper_case_word(self):
        self.assertEqual(rot13("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
                         "NOPQRSTUVWXYZABCDEFGHIJKLM")

    def test_full_alpha(self):
        self.assertEqual(
            rot13("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"),
            "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")


if __name__ == "__main__":
    unittest.main()
