def add(lst):
    summ_lst = []
    for i in range(len(lst)):
        summ_lst.append(sum(lst[:i+1]))
    return summ_lst

    def add(lst):
        return [sum(lst[:result + 1]) for result in range(len(lst))]