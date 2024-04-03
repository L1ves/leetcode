def find_senior(lst):
    # your code here
    max_age = max(developer['age'] for developer in lst)
    return [age for age in lst if age["age"] == max_age]

