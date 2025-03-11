# Step 47: Combine the a-z, A-Z, and 0-9 ranges into a single character class and add a ^ as the first character to negate the pattern.

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
            (special_chars, r'[^a-zA-Z0-9]')
        ]  

# new_password = generate_password(8)
# print(new_password)

pattern = r'\.'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))