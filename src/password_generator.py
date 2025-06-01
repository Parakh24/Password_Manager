"""
Script: password_generator.py


Description:
    This script securely generates a password using `secrets` and `string`,
    encrypts it with `Fernet`, hashes it with `bcrypt`, and stores the hashed
    version in a file using the `os` module.

    
Author: Parakh Virnawe
"""                    
                                      
from cryptography.fernet import Fernet
import string
import bcrypt
import secrets                        
                                          
def generate_password(length):
    """
    Generates a strong password with uppercase, lowercase, digits, and punctuation.
    
    Args:
       length (int): The Length of the desired password (between 8 and 32).
    
    Returns:
        str: A securely shuffled password string.
    """
                                                     
    # Password length Constraints 
    if length < 8 or length > 32:                                           
        raise ValueError("Password length must be between 8 and 32.")         
    
    # length divided into four parts stored in four different variables
    upper = length // 4
    digits = length // 4
    punc = length // 4
    lower = length // 4
        
    # Distribute remaining characters (if not divisible by 4)
    for _ in range(length - (upper + digits + punc + lower)):
        upper += 1 
        digits += 1
        punc += 1
         



    # ''.join -> joins the randomly selected characters into strings
    #  string.ascii_uppercase -> it selects the uppercase letters
    # for _ in range(upper) -> runs the loop the number of times variable stores the uppercase letters
    part_1 = generate_uppercase_part(upper)
    part_2 = generate_digits_part(digits) 
    part_3 = generate_punc_part(punc)
    part_4 = generate_punc_part(lower)


    password_chars = list(part_1 + part_2 + part_3 + part_4)
    secrets.SystemRandom().shuffle(password_chars)  # Cryptographically secure shuffle
    return ''.join(password_chars)


def generate_uppercase_part(upper):
    """
    Generates a string of random uppercase letters.


    Args:
    length (int): number of uppercase letters to generate

    Returns:
    str: A string containing random uppercase letters.
    
    """

# use secrets for secure randomness 
    return ''.join(secrets.choice(string.ascii_uppercase) for _ in range(upper)) 


def generate_digits_part(digits):
    """
    Generates a string of random digits.


    Args:
    length (int): number of digits to generate.

    Return:
    str: A string containing random digits
    
    """

    return''.join(secrets.choice(string.ascii_digits) for _ in range(digits))


def generate_punc_part(punc):
    """
    Generates a string of random punctuation.


    Args:
    length (int): number of punctuation to generate.

    Return:
    str: A string containing random punctuation
    
    """

    return''.join(secrets.choice(string.ascii_punc) for _ in range(punc))


def generate_lowercase_part(lower):
    """
    Generates a string of random lowercase letters

    Args: 
    lower (int): number of lowercase letters

    Return:
    str: A string containing random lowercase letters
    
    """ 

    return ''.join(secrets.choice(string.ascii_lowercase) for _ in range(lower)) 



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



def main():
    """
    Main function to run password generation, encryption, and hashing.

    """
    try: 
    
        
        length = int(input("Enter the length of the password (8-32): "))    
        password = generate_password(length)                              #Calling the Function
        print(f"Generated password: {password}")                          
        
        key = Fernet.generate_key()                                       #Encrypting the Password 
        encrypted_password = encrypt_password(password, key)              
        hashed = hash_password(encrypted_password)
                                                   

    
    except ValueError as e:
        print("Error:", e) 
    

if __name__ == "__main__":
    main() 

