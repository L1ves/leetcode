def remove(s):
    return s[:-1] if s.endswith('!') else s
def remove(s):
    if s:
        if s[-1] == "!":
            return s[:-1]
        else:
            return s
    else:
        return ''