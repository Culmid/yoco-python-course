def rot13(plaintext: str) -> str:
    """Returns the ciphertext resulting from encrypting `plaintext` using the rot13 algorithm"""
    # ... do the encryption...
    return translate(plaintext)


def translate(plaintext: str) -> str:
    ascii_start = 65 if plaintext.isupper() else 97
    return chr((ord(plaintext) - ascii_start + 13) % 26 + ascii_start)
