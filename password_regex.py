

#check password 8 or more charcters contain at least 1 uppercase, 1 lowercase,1 digit ,special symbo1
import re

patt=re.compile("[A-Z]{1}[a-z]{1}[0-9]{1}[^a-zA-Z0-9]")
user_input=input('Enter your password :')
if re.search(patt,user_input):
    print('Valid password,Login successful')
else:
    print('Invalid password')    





#Generate random password which contains at least 1 uppercase, 1lowercase,1 digit,special symbol
import random
import string
import re

# Define the character sets to use in the password
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
special_characters = string.punctuation

# Combine the character sets to form the full pool of characters
all_characters = uppercase_letters + lowercase_letters + digits + special_characters

# Set the desired length of the password
password_length = 10

# Generate a random password
while True:
    password = ''.join(random.choice(all_characters) for _ in range(password_length))

    # Validate the generated password to ensure it meets the requirements
    
    if re.match(r"^[a-zA-Z0-9]+[\.\@\$\%\&\*\-_\+]",password):
        break

print("Random Password:", password)
print('Password strong!')