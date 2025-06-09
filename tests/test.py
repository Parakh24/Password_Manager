import unittest
import sys 
import os
import string

# Add parent directory to sys.path to find 'password_generator.py'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.password_generator import generate_password 


class TestGenerate_Password(unittest.TestCase):
    """
    Class created for Testing(test cases) the password_generator 

    Args:
         unittest.TestCase: 
         A base class in python unittest module which provides all the testing tools required.
    
    """
    def test_easy_length_of_password(self): 
        """
        For testing the easy length of the password
        
        """     
        password = generate_password(10 , "easy")       
        self.assertEqual(len(password) , 10)      
    
    def test_medium_length_of_password(self): 
        """
        For testing the medium length of the password
        
        """  
        password = generate_password(13 , "medium")          
        self.assertEqual(len(password) , 13)           

    def test_hard_length_of_password(self):
        """
        For testing the hard length of the password        
        
        """ 

        password = generate_password(16 , "hard")
        self.assertEqual(len(password) , 16) 


    def test_zero_length_of_password(self):
        """
        For testing the zero length of the password
        
        """
        with self.assertRaises(ValueError):
            generate_password(0 , "easy")
           

    def test_invalid_difficulty(self):  
        """
        For testing the invalid difficulty of the password  
        
        """
        with self.assertRaises(ValueError):
            generate_password(12, "extreme")                                              
    
    def test_easy_only_letters(self):           
        """
        For testing the letters of the "easy" difficulty of the password       
        
        """
  
        password = generate_password(12, "easy")
        self.assertTrue(password.isalpha(), "Easy password should contain only letters")

    def test_medium_contains_letters_digits_and_special(self):  
        """
        For testing the letters , digits and special characters of the "medium" difficulty of the 
        password
            
        """
        password = generate_password(15, "medium")
        has_letter = any(c.isalpha() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)
     
        self.assertTrue(has_letter, "Medium password should contain letters")
        self.assertTrue(has_digit, "Medium password should contain digits")
        self.assertTrue(has_special, "Medium password should contain special characters")

    def test_hard_contains_letters_digits_special_and_extra_symbols(self):
        """
        For testing the letters , digits , special characters and extra_symbols of the "hard"
        difficulty of the password. 
        
        """
        password = generate_password(20, "hard")
        has_letter = any(c.isalpha() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)
        has_extra = any(c in "!@#$%^&*()_+=-" for c in password)
        
        self.assertTrue(has_letter, "Hard password should contain letters")
        self.assertTrue(has_digit, "Hard password should contain digits")
        self.assertTrue(has_special or has_extra, "Hard password should contain special or extra characters")
    
if __name__ == "__main__":
    unittest.main()   