def repeat_elements(list1, list2):
    l1 = set(list1)
    l2 = set(list2)
    return list(l1.intersection(l2))