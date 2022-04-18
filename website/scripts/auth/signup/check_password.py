import re


def check_password(password):
    min_length = 8
    uppercase = True
    lowercase = True
    numbers = True
    special_characters = True

    # check length
    if len(password) < min_length:
        return False
    # look for uppercase
    if uppercase and re.search(r"[A-Z]", password) is None:
        return False
    # look for lowercase
    if lowercase and re.search(r"[a-z]", password) is None:
        return False
    # look for digits
    if numbers and re.search(r"\d", password) is None:
        return False
    # look for special characters
    if special_characters and re.search(r"[ !#$%@&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None:
        return False

    return True
