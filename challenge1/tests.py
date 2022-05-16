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
        self.assertEqual(rot13("nopqrstuvwxyzabcdefghijklm"),
                         "abcdefghijklmnopqrstuvwxyz")

    def test_upper_case_word(self):
        self.assertEqual(rot13("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
                         "NOPQRSTUVWXYZABCDEFGHIJKLM")
        self.assertEqual(rot13("NOPQRSTUVWXYZABCDEFGHIJKLM"),
                         "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def test_full_alpha(self):
        self.assertEqual(
            rot13("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"),
            "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
        self.assertEqual(
            rot13("NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"),
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

    def test_random_word_examples(self):
        words = [["aha", "nun"], ["ant", "nag"], ["balk", "onyx"],
                 ["bar", "one"], ["barf", "ones"], ["be", "or"],
                 ["bin", "ova"], ["ebbs", "roof"], ["envy", "rail"],
                 ["er", "re"], ["errs", "reef"], ["flap", "sync"],
                 ["fur", "she"], ["gel", "try"], ["gnat", "tang"],
                 ["irk", "vex"], ["clerk", "pyrex"], ["purely", "cheryl"],
                 ["png", "cat"], ["sha", "fun"], ["furby", "sheol"],
                 ["terra", "green"], ["what", "jung"], ["url", "hey"],
                 ["purpura", "chechen"], ["shone", "fubar"], ["Ares", "Nerf"],
                 ["abjurer", "nowhere"]]

        for [w1, w2] in words:
            self.assertEqual(rot13(w1), w2)
            self.assertEqual(rot13(w2), w1)

    def test_max_words(self):
        self.assertEqual(rot13("ohvyqvat n jro NCV sebz fpengpu"),
                         "building a web API from scratch")
        self.assertEqual(rot13("n arj fbpvny zrqvn cyngsbez"),
                         "a new social media platform")

    def test_punctuation(self):
        self.assertEqual(rot13("Hello, World!"), "Uryyb, Jbeyq!")


if __name__ == "__main__":
    unittest.main()
