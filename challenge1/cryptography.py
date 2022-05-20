def rot13(plaintext: str) -> str:
    """Returns the ciphertext resulting from encrypting `plaintext` using the rot13 algorithm"""
    return "".join([translateCharacter(c) if c.isalpha() else c for c in plaintext])


def translateCharacter(character: str) -> str:
    ascii_start = 65 if character.isupper() else 97
    return chr((ord(character) + 13 - ascii_start) % 26 + ascii_start)
