# Step 10: Modify your print() call to use the choice() function and pass all_characters as the argument.

import string
import random

# Define the possible characters for the password.
letters = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols
print(all_characters)
print(random.choice(all_characters))