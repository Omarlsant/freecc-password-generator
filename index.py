# Step 8: At the top of your code, import the random module.

import string
import random

# Define the possible characters for the password.
letters = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols
print(all_characters)