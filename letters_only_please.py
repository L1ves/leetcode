import re
def remove_chars(s):
    return  ''.join(re.findall(r"[a-zA-Z\s]+",s))

import re
def remove_chars(s):
    return re.sub(r'[^a-zA-Z ]', '', s)