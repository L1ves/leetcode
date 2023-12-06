# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
#
# Examples
#
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"
def reverse_words(text):
    split_string = string.split(' ')
    reverse_string = ""
    for i in split_string:
        reverse_string += i[::-1] + " "
    return reverse_string[0:-1]


# def reverse_words(str):
#     return ' '.join(s[::-1] for s in str.split(' '))