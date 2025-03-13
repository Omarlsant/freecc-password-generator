# Step 60: Finally, after the for loop, create an if statement to check if count is equal to 4 and break out of the while loop by using the break statement.

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
        for constraint, pattern in constraints:
            if constraint <= len(re.findall(pattern, password)):
                count += 1
        if count == 4:
            break

# new_password = generate_password(8)
# print(new_password)
