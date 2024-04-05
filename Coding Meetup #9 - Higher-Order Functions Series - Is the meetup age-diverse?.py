def is_age_diverse(lst):
    # your code here
    age_group = {
    'teens' : 0,
    'twenties' : 0,
    'thirties' : 0,
    'forties' : 0,
    'fifties' : 0,
    'sixties' : 0,
    'seventies' : 0,
    'eighties' : 0,
    'nineties' : 0,
    'centenarian' : 0
}
    for i in lst:
        age = i['age']
        if age < 20:
            age_group['teens'] = 1
        elif age < 30:
            age_group['twenties'] = 1
        elif age < 40:
            age_group['thirties'] = 1
        elif age < 50:
            age_group['forties'] = 1
        elif age < 60:
            age_group['fifties'] = 1
        elif age < 70:
            age_group['sixties'] = 1
        elif age < 80:
            age_group['seventies'] = 1
        elif age < 90:
            age_group['eighties'] = 1
        elif age < 100:
            age_group['nineties'] = 1
        else:
            age_group['centenarian'] = 1

    for i in age_group.values():
        if i == 0:
            return False
    return True


def is_age_diverse(lst):
    arr = list(map(lambda x: x["age"] // 10, lst))
    return any(x >= 10 for x in arr) and all(i in arr for i in range(1, 10))