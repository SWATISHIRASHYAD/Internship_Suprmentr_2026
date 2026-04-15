#Assignment for today - 7th Feb 2026 Create a strong code for password authentication using python. 
import re
import hashlib
import getpass

def is_strong_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one digit"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character"
    
    return True, "Strong password"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

stored_password_hash = None

def register():
    global stored_password_hash
    print("\n--- User Registration ---")
    
    while True:
        password = getpass.getpass("Enter a strong password: ")
        valid, message = is_strong_password(password)
        
        if valid:
            confirm = getpass.getpass("Confirm password: ")
            if password == confirm:
                stored_password_hash = hash_password(password)
                print("✅ Registration successful!\n")
                break
            else:
                print("❌ Passwords do not match. Try again.\n")
        else:
            print(f"❌ {message}\n")

def login():
    print("\n--- User Login ---")
    attempts = 3
    
    while attempts > 0:
        password = getpass.getpass("Enter your password: ")
        if hash_password(password) == stored_password_hash:
            print("✅ Login successful!\n")
            return
        else:
            attempts -= 1
            print(f"❌ Incorrect password. Attempts left: {attempts}")
    
    print("🚫 Too many failed attempts. Access denied.\n")

# Main program
def main():
    register()
    login()

if __name__ == "__main__":
    main()