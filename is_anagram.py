# Is Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Example 1:
#
# Input: s = "racecar", t = "carrace"
#
# Output: true
# Example 2:
#
# Input: s = "jar", t = "jam"
#
# Output: false
# Constraints:
#
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            str1 = sorted(s.lower())
            str2 = sorted(t.lower())
            if str1 == str2:
                return True
            else:
                return False
# sort and make lowercase then equal


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t)