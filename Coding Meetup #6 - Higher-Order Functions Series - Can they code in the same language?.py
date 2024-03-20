def is_same_language(lst):
    language = lst[0]['language']
    for person in lst:
        if person['language'] != language:
            return False
    return True

def is_same_language(lst):
    return len(set(i["language"] for i in lst)) == 1