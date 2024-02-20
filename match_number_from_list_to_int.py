import re
def get_number_from_string(st):
    answer = ''.join(re.findall(r'[\d]+',st)).split(',')
    answer = map(int,answer)
    for x in answer:
        return x

def get_number_from_string(string):
    return int(''.join(x for x in string if x.isdigit()))