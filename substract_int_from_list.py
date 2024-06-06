def div_con(y):
    return sum(x for x in y if isinstance(x, int)) - sum(int(x) for x in y if isinstance(x, str))

def div_con(y):
    # your code here
    string_sort = []
    for i in y:
        if i == str(i):
            string_sort.append(int(i))
    string_num2 = list(filter(lambda x: not isinstance(x, str), y))
    return (sum(string_num2) - sum(string_sort))