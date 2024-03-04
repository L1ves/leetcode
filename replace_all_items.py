def replace_all(obj, find, replace):
    if type(obj) == str:
        obj = list(obj)
        l = list(map(lambda x: x.replace(find, replace), obj))
        return (''.join(l))
    if type(obj) == list:
        for i in range(len(obj)):
            if obj[i] == find:
                obj[i] = replace
        return obj

def replace_all(obj, old, new):
    try:
        return obj.replace(old, new)
    except:
        return [i if i != old else new for i in obj]