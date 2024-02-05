import re
def to_camel_case(string):
    #camel = re.findall(r'\w+',text)
    if string:
        if string[0].islower():
            camel_split_step_1 = ''.join(string.title().split('_'))
            camel_split_step_2 = ''.join(camel_split_step_1.split('-'))
            return (camel_split_step_2[0].lower() + camel_split_step_2[1:])
        if string[0].isupper():
            camel_split_step_1 = ''.join(string.title().split('_'))
            camel_split_step_2 = ''.join(camel_split_step_1.split('-'))
            return (''.join(camel_split_step_2.split('-')))
    else:
        return ''


def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])
def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')