import re
def validate_usr(username):
    #your code here
    return True if re.match(r"^[a-z0-9_]{4,16}$",username) else False