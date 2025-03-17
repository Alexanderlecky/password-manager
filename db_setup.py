import sqlite3
from encryption import encrypt_password, decrypt_password

def init_db():
    """Initialize the SQLite database and create the passwords table."""
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def store_password(website, username, password):
    """Stores an encrypted password in the database."""
    encrypted_password = encrypt_password(password)
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
                   (website, username, encrypted_password))
    conn.commit()
    conn.close()
    print("✅ Password stored successfully!")

def retrieve_password(website):
    """Retrieves and decrypts a password from the database."""
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM passwords WHERE website = ?", (website,))
    result = cursor.fetchone()
    conn.close()
    if result:
        username, encrypted_password = result
        decrypted_password = decrypt_password(encrypted_password)
        print(f"🔑 Website: {website}\n👤 Username: {username}\n🔐 Password: {decrypted_password}")
    else:
        print("❌ No credentials found for this website.")
