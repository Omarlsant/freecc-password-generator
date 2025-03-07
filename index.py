# Step 12: Although the effect might seem equal to random.choice(), secrets ensure you the most secure source of randomness that your operating system can provide. Now, delete your two print() calls.

import secrets
import string

# Define the possible characters for the password.
letters = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols
