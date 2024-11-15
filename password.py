import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define character sets based on user preferences
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Create the pool of characters based on what the user wants
    characters = lowercase
    if use_uppercase:
        characters += uppercase
    if use_digits:
        characters += digits
    if use_special_chars:
        characters += special_chars

    # Ensure the password length is at least 1
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    # Randomly select characters from the pool and join them into a password string
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# User input for password generation
length = int(input("Enter password length: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

# Generate and display the password
password = generate_password(length, use_uppercase, use_digits, use_special_chars)
print(f"Generated password: {password}")
