def accum(s):
    # your code
    new_string = ""
    for index, char in enumerate(s):
        new_string += char.capitalize() + (char.lower() * index) + "-"
    return new_string[:-1]

# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))