# return masked string
def maskify(cc):
    hash_list = []
    for i in range(len(cc)-4):
        i = '#'
        hash_list.append(i)
    return ''.join(hash_list) + cc[-4:]