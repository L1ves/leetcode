def remove_duplicate_words(s):
    s = s.split()
    remove = []
    for i in s:
        if i not in remove:
            remove.append(i)
    return ' '.join(remove)

def remove_duplicate_words(s):
    return ' '.join(dict.fromkeys(s.split()))