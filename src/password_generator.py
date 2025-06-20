"""
Script: password_generator.py


Description:
    This script securely generates a password using `secrets` and `string`,
    encrypts it with `Fernet`, and stores the encrypted password along with the
    version in a file using the `os` module.

    
Author: Parakh Virnawe 

"""                    
                                                                                         
from cryptography.fernet import Fernet    
import string         
import secrets 
import os                                                                                                            
                                           
def generate_password(length , difficulty):
    """
    Generates a strong password with uppercase, lowercase, digits, and punctuation. 
    Creates  on the basis of the difficulty level i.e. easy , medium and hard. 


    Args:
       length (int): The Length of the desired password (between 8 and 32). 
       difficulty (str): The difficulty level of the password (easy, medium , hard).

    Returns:
        str: A securely shuffled password string.
    """
                                                     
    # Password length Constraints 
    if length < 8 or length > 32:                                           
        raise ValueError("Password length must be between 8 and 32.")         
    


    # ''.join -> joins the randomly selected characters into strings
    # string.ascii_letters + string.digits -> it selects the letters(uppercase and lowercase)+ digits
    # for _ in range(upper) -> runs the loop the number of times variable stores the letters and digits
    if difficulty == "easy":
        password_chars = string.ascii_letters + string.digits                      
        return ''.join(secrets.choice(password_chars) for _ in range(length))      

    elif difficulty == "medium":
        password_chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(password_chars) for _ in range(length))

    elif difficulty == "hard":  
    
    # length divided into four parts stored in four different variables
     upper = length // 4
     digits = length // 4
     punc = length // 4
     lower = length // 4                    
                                                                                              
    # Distribute remaining characters (if not divisible by 4)
     leftovers = length - (upper + digits + punc + lower)
     for i in range(leftovers):
        if i == 0:
            upper += 1
        elif i == 1:
            digits += 1
        elif i == 2:
            punc += 1            
         
                         
     part_1 = generate_uppercase_part(upper)
     part_2 = generate_digits_part(digits) 
     part_3 = generate_punc_part(punc)
     part_4 = generate_lowercase_part(lower)
    
    
     password_chars = list(part_1 + part_2 + part_3 + part_4)
     secrets.SystemRandom().shuffle(password_chars)  # Cryptographically secure shuffle
     return ''.join(password_chars)
    
    else:
        raise ValueError("Invalid difficulty level. Please choose 'easy', 'medium' or 'hard' .") 
        
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

    return''.join(secrets.choice(string.digits) for _ in range(digits))


def generate_punc_part(punc):
    """
    Generates a string of random punctuation.


    Args:
    length (int): number of punctuation to generate.

    Return:
    str: A string containing random punctuation
    
    """

    return''.join(secrets.choice(string.punctuation) for _ in range(punc))



def generate_lowercase_part(lower):
    """
    Generates a string of random lowercase letters

    Args: 
    lower (int): number of lowercase letters

    Return:
    str: A string containing random lowercase letters
    
    """ 

    return ''.join(secrets.choice(string.ascii_lowercase) for _ in range(lower)) 

    
def encrypted_password(password):
    """
    Encrypts the password using Fernet.
    
    Args:
        password (str): The password to be encrypted.
        key (bytes): The encryption key.

    Returns:
        bytes: Encrypted password. 

    """
    if not os.path.exists("key.key"):
     key = Fernet.generate_key() 
     with open("key.key", "wb") as key_file:
        key_file.write(key)
    
    else:  
       with open("key.key", "rb") as key_file:
        key = key_file.read()

        fernet = Fernet(key)

       encrypted = fernet.encrypt(password.encode())
       return encrypted
    

def save_password_to_file(service , encrypted): 
                                                                                                                           
    """                                                                                                   
    Saves the generated, encrypted, and hashed password to a file in binary mode.
    
    Args:
        hashed (bytes): The hashed password (bcrypt).
        encrypted (bytes): The encrypted password (Fernet).

    """
    try:
        with open("password.secure", "ab") as file:
         file.write(b"Service: " + service.encode() + b"\n")
         file.write(b"Encrypted Password: " + encrypted + b"\n")
         file.write(b"-" * 40 + b"\n")
                                                                    
    except Exception as e:
        print("Error:", e)                                            


def main():
    """
    Main function to run password generation and encryption. 

    """
    try: 
        service = str(input("Enter the service name: ")).strip()
        length = int(input("Enter the length of the password (8-32): ")) 
        difficulty = input("Enter the difficulty level (easy , medium , hard): ")   
        password = generate_password(length , difficulty)                              #Calling the Function
        print(f"Generated password: {password}")                         
        
        encrypted = encrypted_password(password)                                       #for encryption
        #print(f"Encrypted Password: {encrypted}")
                                                                                             
        
        save_password_to_file(service,encrypted)
    
    except ValueError as e:
        print("Error:", e)                                   
    

if __name__ == "__main__":
    main()                                   
              
    