def evklid(x,y):
    if y == 0:
        x, y = y, x
    while y != 0:
        x, y = y, x % y
    return x

evklid(15,5)
