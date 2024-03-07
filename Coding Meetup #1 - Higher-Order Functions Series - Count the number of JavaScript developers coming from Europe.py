def count_developers(lst):
    score = 0
    for person in lst:
        if person["continent"] == "Europe" and person["language"] == "JavaScript":
            score +=1
    return score

def count_developers(lst):
    return sum(x["language"] == "JavaScript" and x["continent"] == "Europe" for x in lst)