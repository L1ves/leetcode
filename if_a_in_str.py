# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
#
# Examples:
#
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false
def solution(text, ending):
    # your code here...
    return True if ending in text and text[-1] == ending[-1] else False

def solution(string, ending):
    return string.endswith(ending)