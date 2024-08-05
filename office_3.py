def broken(inp):
    #x = ' '.join(string)
    new_string = []
    for i in inp:
        if i == '0':
            new_string.append('1')
        if i == '1':
            new_string.append('0')
    return ''.join(new_string)

def broken(inp):
    return ''.join(['0' if i == '1' else '1' for i in inp])