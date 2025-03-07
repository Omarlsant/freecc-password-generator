# Step 14: Your generate_password function needs a few parameters. Start by adding a length parameter.

import secrets
import string

def generate_password(length):
    # Define the possible characters for the password.
    letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols
