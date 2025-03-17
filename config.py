import os
from cryptography.fernet import Fernet

def load_key():
    """Generate a new encryption key or load an existing one."""
    key_file = "key.key"

    if not os.path.exists(key_file):
        key = Fernet.generate_key()  # Generate a 32-byte key
        with open(key_file, "wb") as f:
            f.write(key)
    else:
        with open(key_file, "rb") as f:
            key = f.read()
        
        # Validate key length (Must be 32 bytes)
        if len(key) != 44:  # Base64 encoding makes 32-byte key into 44 characters
            print("❌ Invalid encryption key detected! Regenerating...")
            os.remove(key_file)
            return load_key()  # Re-run key generation

    return key

# Load encryption key
encryption_key = load_key()
