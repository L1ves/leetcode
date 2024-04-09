def get_average(lst):
    # your code here
    return round(sum(age['age'] for age in lst) / len(lst))
