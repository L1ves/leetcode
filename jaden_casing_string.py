def to_jaden_case(string):
    # ...
    return ' '.join([x.capitalize() for x in string.split()])

import string
toJadenCase = string.capwords