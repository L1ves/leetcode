import re
def is_it_a_num(s: str) -> str:
    matcher = ''.join(re.findall(r'[0-9]+',s))
    if len(matcher) == 11:
        if matcher.startswith('0'):
            return matcher
        else:
            return "Not a phone number"
    else:
        return "Not a phone number"


import re
def is_it_a_num(s: str) -> str:
    matcher = ''.join(re.findall(r'[0-9]+',s))
    return matcher if len(matcher) == 11 and matcher.startswith('0') else "Not a phone number"

def is_it_a_num(s: str) -> str:
    t = ''.join(i for i in s if i.isdigit())
    return t if len(t)==11 and t[0]=="0" else "Not a phone number"