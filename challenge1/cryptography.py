def rot13(plaintext: str) -> str:
    """Returns the ciphertext resulting from encrypting `plaintext` using the rot13 algorithm"""
    # ... do the encryption...
    return chr(ord(plaintext) + 13)
