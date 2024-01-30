def add(s1, s2):
    counter1 = 0
    counter2 = 0
    for i in s1:
        counter1 += ord(i)
    for j in s2:
        counter2 += ord(j)
    return counter1 + counter2

def add(s1, s2):
    return sum(ord(x) for x in s1+s2)