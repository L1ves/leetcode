def count_languages(lst):
    # your code here

    new_dict = {}
    for i in lst:
        language = i["language"]
        if language in new_dict:
            new_dict[language] += 1
        else:
            new_dict[language] = 1
    return new_dict

    from collections import Counter
    def count_languages(lst):
        return Counter([d['language'] for d in lst])