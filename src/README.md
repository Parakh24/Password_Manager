# Password Manager Code

The password manager in the src module uses the following logic to generate strong, secure passwords:

**User-Defined Length with Constraints:**

1. The user inputs the desired password length.

2. The length must lie within a minimum and maximum threshold (e.g., 8 to 32 characters).

3. If the input does not meet these conditions, the program raises a warning or prompts for a valid input.

**Password Composition (Divided into Four Parts)
The valid length is evenly divided into four sections:**

1. **Uppercase Letters:** (A-Z)

   The first quarter of the password includes randomly selected uppercase alphabets.

2. **Special Character:** (!, @, #, $, etc.)

   The second quarter includes a variety of special characters to increase security.

3. **Digits:** (0-9)

   The third quarter consists of numeric digits.

4. **Lowercase Letters:** (a-z)

    The final quarter includes lowercase alphabets.

**Password Shuffling:**

1. After constructing the password from all four segments,   the characters are shuffled to ensure randomness and avoid predictable patterns.

**Output:**

1. The final password is displayed or stored securely for the user.  
