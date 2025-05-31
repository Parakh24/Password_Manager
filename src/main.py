
                                                                                                                                                                        
from cryptography.fernet import fernet
import os                                
import string                            
import bcrypt                                                
import secrets 

                                                                    

Password_length = int(input("Enter the length of the password: "))  

if Password_length < 8 or Password_length > 32:                     
    print("Error: Password length must be between 8 and 32 characters.")
    exit()

# Divide the password length into 4 parts 

upper = Password_length // 4
digits = Password_length // 4 
punc = Password_length // 4
lower = Password_length // 4 

if(Password_length % 4 != 0):
    upper += 1
    digits += 1
    punc += 1 
    lower += 1 

# generate the string for all the four parts of the password 

part_1 = ''.join(secrets.choice(string.ascii_uppercase) for _ in range(upper))
part_2 = ''.join(secrets.choice(string.ascii_digits) for _ in range(digits))
part_3 = ''.join(secrets.choice(string.ascii_punctuation) for _ in range(punc))
part_4 = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(lower))    



password_chars = part_1 + part_2 + part_3 + part_4 

#Generated_password i.e. shuffled 
Generated_password = secrets.choice(password_chars) 


#in order to encrypt a password
Encrypted_password = fernet.encrypt(Generated_password.encode()) 


#Hashing
Hashed = bcrypt.hashpw(Encrypted_password, bcrypt.gensalt)

#Checking
bcrypt.checkpw(Encrypted_password, Hashed)




# Use os to create a secure file path and save encrypted password

os.makedirs("secure_data", exist_ok=True)
file_path = os.path.join("secure_data", "Hashed.txt")

with open(file_path, "wb") as f:
    f.write(Hashed)

print(f"Encrypted password saved to: {file_path}")      



