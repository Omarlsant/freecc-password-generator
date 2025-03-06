# Step 9: Call the random() function from the random module and print the result.

import string
import random

# Define the possible characters for the password.
letters = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols
print(all_characters)
print(random.random())