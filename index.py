# Step 61: Replace your existing for loop and two if statements with a single if statement. For the if condition, use a call to the all() function and pass an empty list as the argument to the function call.

import re
import secrets
import string

def generate_password(length, nums, special_chars, uppercase, lowercase):
    # Define the possible characters for the password.
    letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols
    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        constraints = [
            (nums, r'\d'),
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]'),
            (special_chars, fr'[{symbols}]')
        ]
        # Check constraints
        count = 0
        if all([]):
            break
    return password

# new_password = generate_password(8)
# print(new_password)
