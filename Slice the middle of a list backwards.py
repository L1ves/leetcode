def reverse_middle(lst):
    if len(lst) % 2 == 0:
        count = len(lst) // 2
        lst.reverse()
        return lst[count-1:count +1]
    else:
        count = len(lst) // 2
        lst.reverse()
        return lst[count-1:int(count)+2:]

#refactored
    def reverse_middle(lst):
        return lst[len(lst) // 2 - 1:len(lst) // 2 + 1:][::-1] if len(lst) % 2 == 0 else lst[len(lst) // 2 - 1:len(lst) // 2 + 2:][::-1]

def reverse_middle(lst):
    l = len(lst)//2 - 1
    return lst[l:-l][::-1]

def reverse_middle(lst):
    l = len(lst)//2 - 1
    return lst[-l:l-2:-1]