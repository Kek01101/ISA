# 16/9/2020, Blue, Nicolas Keck, Takes an array of potential passwords and print out the bad ones
# Extension: Allows passwords with all types of special characters
import string
from copy import deepcopy
passwords = [123456789, "Joe", "Jimyty!23", "Password", ",./.,';/1/'", "Epic_gamer_123"]
print("Bad passwords:")
for password in deepcopy(passwords):
    digit = False
    spechar = False
    if len(str(password)) > 8:
        for character in str(password):
            if character in string.digits:
                digit = True
            elif character in string.punctuation:
                spechar = True
            if digit and spechar:
                break
        if not digit or not spechar:
            print(password)
            passwords.remove(password)
    else:
        print(password)
        passwords.remove(password)
print(f"\nAccepted passwords:\n{passwords}")