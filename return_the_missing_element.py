def get_missing_element(seq):
    # your code here

    ten = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
    new_seq = set(sorted(seq))
    set_seq = ten.difference(new_seq)
    return next(iter(set_seq))

def get_missing_element(seq):
    return 45 - sum(seq)


def get_missing_element(seq):
    for i in range(0, 10):
        if not i in seq: return i