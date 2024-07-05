def return_dups(a_list):
    dups = []
    a_set = set()
    for item in a_list:
        l1 = len(a_set)
        a_set.add(item)
        l2 = len(a_set)
        if l1 == l2:
            dups.append(item)
    return dups

