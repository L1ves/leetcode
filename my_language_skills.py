# Task
#
# You are given a dictionary/hash/object containing some languages and your test results in the given languages. Return the list of languages where your test score is at least 60, in descending order of the scores.
#
# Note: the scores will always be unique (so no duplicate values)
#
# Examples
#
# {"Java": 10, "Ruby": 80, "Python": 65}    -->  ["Ruby", "Python"]
# {"Hindi": 60, "Dutch" : 93, "Greek": 71}  -->  ["Dutch", "Greek", "Hindi"]
# {"C++": 50, "ASM": 10, "Haskell": 20}     -->  []

def my_languages(results):
    # your fantastic code here
    more_than_60 = []
    for value, items in results.items():
        if items >= 60:
            more_than_60.append((value, items))
    more_than_60.sort(key=lambda x: x[1], reverse=True)
    sorted_language = [language for language, _  in more_than_60]
    return sorted_language