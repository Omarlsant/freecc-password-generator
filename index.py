# Step 16: Below your new variable, add a comment saying Generate password.

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
