# Step 5: Now declare a variable named all_characters and assign it the result of concatenating your existing variables.

import string

# Define the possible characters for the password.
letters = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols