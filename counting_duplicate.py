def most_frequent(data: list[str]) -> str:
    # your code here
    empty_dict = {}
    for i in data:
        if i in empty_dict:
            empty_dict[i] += 1
        else:
            empty_dict[i] = 1

    return max(empty_dict, key=empty_dict.get)


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")


def duplicate_count(text):
    new_counter = 0
    empty_dict = {}
    # Your code goes here
    if len(text) > 0:
        new_text = ' '.join(text.lower()).split()
        #ставим указатель на каждый елемент списка
        for i in new_text:
            if i in empty_dict:
                empty_dict[i] += 1
            else:
                empty_dict[i] = 1
                    # но counter может быть > 2,3,10  а нам нужно посчитать все вхождения за единицу
        for x in empty_dict.values():
            if x > 1:
                new_counter += 1
                    # надо обнулить счетчик
    return new_counter