# Step 62: Right now, all() is taking an empty list as the argument. Populate that empty list using the comprehension syntax so that the list stores the results of evaluating the expression constraint, for each constraint-pattern tuple in the constraints list.

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
        if all([constraint <= len(re.findall(pattern, password)) for constraint, pattern in constraints]):
            break
    return password

# new_password = generate_password(8)
# print(new_password)
