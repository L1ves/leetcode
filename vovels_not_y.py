def get_count(sentence):
    new_sentence = ' '.join(sentence.split(' '))
    counter = 0
    vovels = ['a', 'e', 'i', 'o', 'u']
    if len(sentence) > 0:
        for i in new_sentence:
            if i in vovels:
                counter += 1
        return counter
    else:
        return 0

# def getCount(s):
#     return sum(c in 'aeiou' for c in s)