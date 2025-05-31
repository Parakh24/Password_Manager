"""
Script: password_generator.py


Description:
    This script securely generates a password using `secrets` and `string`,
    encrypts it with `Fernet`, hashes it with `bcrypt`, and stores the hashed
    version in a file using the `os` module.

    
Author: Parakh Virnawe
"""

from cryptography.fernet import Fernet
import os
import string
import bcrypt
import secrets

def generate_password(length):
    """
    Generates a strong password with uppercase, lowercase, digits, and punctuation.
    
    Args:
        length (int): Length of the desired password (between 8 and 32).
    
    Returns:
        str: A securely shuffled password string.
    """
    if length < 8 or length > 32:
        raise ValueError("Password length must be between 8 and 32.")

    upper = length // 4
    digits = length // 4
    punc = length // 4
    lower = length // 4

    # Distribute remaining characters (if not divisible by 4)
    for _ in range(length - (upper + digits + punc + lower)):
        upper += 1  # You could alternate which section gets the extra if you want more balance

    part_1 = ''.join(secrets.choice(string.ascii_uppercase) for _ in range(upper))
    part_2 = ''.join(secrets.choice(string.digits) for _ in range(digits))
    part_3 = ''.join(secrets.choice(string.punctuation) for _ in range(punc))
    part_4 = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(lower))

    password_chars = list(part_1 + part_2 + part_3 + part_4)
    secrets.SystemRandom().shuffle(password_chars)  # Cryptographically secure shuffle
    return ''.join(password_chars)


def encrypt_password(password, key):
    """
    Encrypts the password using Fernet.
    
    Args:
        password (str): The plain password to encrypt.
        key (bytes): The Fernet key.
    
    Returns:
        bytes: Encrypted password.
    """
    fernet = Fernet(key)
    return fernet.encrypt(password.encode())


def hash_password(encrypted_password):
    """
    Hashes the encrypted password using bcrypt.
    
    Args:
        encrypted_password (bytes): The encrypted password.
    
    Returns:
        bytes: Hashed password.
    """
    return bcrypt.hashpw(encrypted_password, bcrypt.gensalt())


def save_to_file(data, path="secure_data/Hashed.txt"):
    """
    Saves binary data to a file at the given path.
    
    Args:
        data (bytes): Data to be written.
        path (str): File path to save to.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)


def main():
    """
    Main function to run password generation, encryption, and hashing.

    """
    try:
        length = int(input("Enter the length of the password (8–32): "))  
        password = generate_password(length) 
        print(f"Generated password: {password}")      

        key = Fernet.generate_key()
        encrypted_password = encrypt_password(password, key)
        hashed = hash_password(encrypted_password)
                                                   
        save_to_file(hashed)
        print("✅ Encrypted and hashed password saved to 'secure_data/Hashed.txt'")

    except ValueError as e:
        print("Error:", e)
    

if __name__ == "__main__":
    main()
