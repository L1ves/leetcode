import string
def ceasar(a_string, key):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase

    encrypt = ''
    for c in a_string:
        if c in uppercase:
            new = (uppercase.index(c) + key) % 26
            encrypt += uppercase[new]
        elif c in lowercase:
            new = (lowercase.index(c) + key) % 26
            encrypt += lowercase[new]

        else:
            encrypt += c
    return encrypt
