# Step 41: Add one last tuple to your list. Use the special_chars parameter as the first item and an empty string as the second item.

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
            (nums, '[0-9]'),
            (lowercase, '[a-z]'),
            (uppercase, '[A-Z]'),
            (special_chars, '')
        ]   

# new_password = generate_password(8)
# print(new_password)

pattern = '[^a-z]t'
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))