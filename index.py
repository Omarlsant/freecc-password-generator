# Step 6: Your all_characters variable is a string formed by all lowercase and uppercase letters, all the 10 digits and several special characters. Just before it, add a comment saying Combine all characters.

import string

# Define the possible characters for the password.
letters = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols