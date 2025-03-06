# Step 7: Now print the all_characters variable to see what it looks like.

import string

# Define the possible characters for the password.
letters = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols
print(all_characters)