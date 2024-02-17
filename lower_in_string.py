def lowercase_count(strng):
    return sum(a.islower() for a in strng)

import re
def lowercase_count(string):
    return len(re.findall('[a-z]',string))

def lowercase_count(strng):
    # Your code here
    counter = 0
    for i in strng:
        if i.islower():
            counter += 1
    return counter