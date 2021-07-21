import string
import random

all_alpha_characters = string.ascii_letters
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

all_numeric_characters = string.digits
# 0123456789

all_special_characters = string.punctuation
# !”#$%&'()*+,-./:;<=>?@[]^_`{|}~

all_valid_characters = all_alpha_characters + \
    all_special_characters + all_numeric_characters
# all valid alphabets, numbers & special characters

password = "".join(random.choice(all_valid_characters)
                   for iterator in range(random.randint(10, 16)))
# generating random character of password

print("The Password is: " + password)
