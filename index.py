# Step 72: Finally, put the last two lines of your code inside an if statement that execute when __name__ == '__main__'. In this way, your code won't run when imported as a module. Otherwise, it will call generate_password() and print the generated password.

import re
import secrets
import string

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
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

if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)