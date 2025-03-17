import getpass
from db_setup import init_db, store_password, retrieve_password

def main():
    """CLI-based Password Manager."""
    init_db()  # Ensure database is set up

    while True:
        print("\n🔒 Password Manager")
        print("1️⃣ Store Password")
        print("2️⃣ Retrieve Password")
        print("3️⃣ Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            website = input("🌐 Enter website: ")
            username = input("👤 Enter username: ")
            password = getpass.getpass("🔑 Enter password: ")  # Hides input
            store_password(website, username, password)

        elif choice == "2":
            website = input("🌐 Enter website to retrieve credentials: ")
            retrieve_password(website)

        elif choice == "3":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
