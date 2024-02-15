import re
def string_clean(s):
    valid_string = r"\D"
    return ''.join(re.findall(valid_string,s))

def string_clean(s):
    return ''.join(x for x in s if not x.isdigit())
