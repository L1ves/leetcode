
#Наименьшее общее делимое
def nodM(d1,d2):
    gcf = None
    if d1 == 0:
        d2 = gcf
    if d2 == 0:
        d1 = gcf
    if d1 < 0 or d2 < 0:
        raise ValueError("Numbers must be positive")
    if d1 > d2:
        smaller = d2
    else:
        smaller = d1
    for i in range(1, smaller + 1):
        if (d1 % i == 0) and (d2 % i == 0):
            gcf = i
    return gcf


20, 5