def remove_smallest(lst):
    if lst:
        new_list = lst.copy()
        min_sum = min(new_list)
        new_list.remove(min_sum)
        return new_list
    else:
        return []

def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a