# Step 19: After the loop, add a return statement to your function so it returns the password variable.

import secrets
import string

def generate_password(length):
    # Define the possible characters for the password.
    letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols
    password = ''
    # Generate password

    for _ in range(length):
        password += secrets.choice(all_characters)
        return password
