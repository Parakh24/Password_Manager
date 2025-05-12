# 🔐Password Generation Logic

    Our Password Manager generates strong, secure passwords using a mix of the following character 
    sets: 

**Alphabets:**

         1. Uppercase: A–Z
         2. Lowercase: a–z

**Numbers:**

         1. Digits: 0–9

**Special Characters:**

         1. Common symbols like: ! @ # $ % ^ & * ( ) _ + - = { } [ ] : ; < > , . ? / | \ 

## Password Length Constraints

To ensure strong and secure passwords, the Password Manager allows the user to customize the password length, but within safe boundaries.

✅ Rules for Password Length:

     Minimum Length (Threshold): 8 characters

     Maximum Length (Constraint): 32 characters

     User must choose a length within this range for 
     the password to be generated.

**If a user enters a length below 8 or above 32, the system will:**

     Prompt the user to enter a valid length again or automatically generate a password using the 
     default length (e.g., 12 characters)
