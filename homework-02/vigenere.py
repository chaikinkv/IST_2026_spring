from caesar import encrypt_caesar, decrypt_caesar
from string import ascii_lowercase, ascii_uppercase


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    
    
    cipher_text = ""
    
    abc_upper = ascii_uppercase
    abc_lower = ascii_lowercase
    n = len(keyword)
    password = [abc_upper.index(i) if i.isupper() else abc_lower.index(i) for i in keyword]
    cipher_text = list(plaintext)
  
    for i in range(n):
        cipher_text[i::n] = encrypt_caesar(plaintext[i::n], password[i])
    cipher_text = "".join(cipher_text)
    return cipher_text
    


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ciphertext
    
    
    abc_upper = ascii_uppercase
    abc_lower = ascii_lowercase
    n = len(keyword)
    password = [abc_upper.index(i) if i.isupper() else abc_lower.index(i) for i in keyword]
    cipher_text = list(plaintext)
  
    for i in range(n):
        cipher_text[i::n] = decrypt_caesar(plaintext[i::n], password[i])
    cipher_text = "".join(cipher_text)
    return cipher_text
