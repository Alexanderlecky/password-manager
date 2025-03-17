from cryptography.fernet import Fernet
from config import encryption_key

cipher = Fernet(encryption_key)

def encrypt_password(password):
    """Encrypts a password using Fernet."""
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    """Decrypts an encrypted password."""
    return cipher.decrypt(encrypted_password.encode()).decode()
