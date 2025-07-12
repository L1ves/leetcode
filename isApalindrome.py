import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = "\w+"
        s = re.findall(pattern, s)
        s = ''.join(s).lower()
        return True if s == s[::-1].lower() else False

new_str = ''
for s in strStr:
    if s.isalnum():
        new_str += s.lower()
        return new_str == new_str[::-1]
