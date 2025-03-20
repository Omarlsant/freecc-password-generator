# Step 67: As long as all the arguments in a function call are keyword arguments, the order of the arguments doesn't matter. To confirm this, try to change the order of length=8 and nums=1 in your function call.

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
        if all(
            constraint <= len(re.findall(pattern, password))
                for constraint, pattern in constraints
        ):
            break
    return password

new_password = generate_password(nums=1, length=8, special_chars=1, uppercase=1, lowercase=1)
print(new_password)