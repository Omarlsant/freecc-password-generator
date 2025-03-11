# Step 50: The space characters and the final period are matched, as they are the only non-alphanumeric characters in the string. Now turn your quote string into a single underscore character.

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
            (special_chars, r'\W')
        ]  

# new_password = generate_password(8)
# print(new_password)

pattern = r'\W'
quote = '_'
print(re.findall(pattern, quote))