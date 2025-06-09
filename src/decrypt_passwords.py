from cryptography.fernet import Fernet 
import os


def decrypted_password(enc_password):
    """
    Decrypts the encrypted password using Fernet.
    
    Args:
        enc_password (bytes): The encrypted password.
        key (bytes): The encryption key.

    Returns:
        str: Decrypted password.
    """
    if not os.path.exists("key.key"):
     key = Fernet.generate_key() 
     with open("key.key", "wb") as key_file:
        key_file.write(key)

    else:  
       with open("key.key", "rb") as key_file:
        key = key_file.read()

        fernet = Fernet(key)

       decrypted = fernet.decrypt(enc_password).decode()
       return decrypted 
    

def decrypt_specific_service(): 
    """
    This function decrypts the encrypted password of a specific service.
        
    """
    target_service = input("Enter the service name you want to decrypt the password for: ").strip().lower()

    with open("password.secure", "rb") as file:
        lines = file.readlines()

    current_service = None
    found = False
    
    for i in range(len(lines)):
        line = lines[i].strip()

        if line.startswith(b"Service:"):
            current_service = line.split(b"Service:")[1].strip().decode().lower()

        if current_service == target_service and line.startswith(b"Encrypted Password:"):
            encrypted = line.split(b"Encrypted Password:")[1].strip()
            try: 
                decrypted = decrypted_password(encrypted)
                print(f"\n Decrypted password for '{target_service}': {decrypted}")
                found = True
                break
            except Exception as e:
                print(f" Error while decrypting: {e}")
                found = True
                break

    if not found:
        print(f" No password found for service: {target_service}")



if __name__ == "__main__":
    decrypt_specific_service()
