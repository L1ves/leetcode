def get_middle(s):
    if len(s) == 2:
        return s
    if len(s) % 2 == 0:
        average =  len(s) // 2
        return s[average-1] + s[average]
    if len(s) % 2 != 0:
        average =  (len(s)-1) // 2
        return s[average]

def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]