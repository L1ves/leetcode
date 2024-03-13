def is_ruby_coming(lst):
    # your code here
    return any(dev['language'] == 'Ruby' for dev in lst)

    # for dev in lst:
    #     if dev['language'] == 'Ruby':
    #         return True
    #     return False
    # # your code here