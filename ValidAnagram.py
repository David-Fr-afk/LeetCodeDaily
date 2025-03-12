'''
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        if sorted(t) == sorted(s): 
            return True
        else:
            return False
   '''
   # the solution above is the one i found by myself, the one below is the more optimal solution that uses a hash map which I had to learn\
   # At least I know hashmaps now though!!     
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        char_map = {}
        for char in s:
            char_map[char] = char_map.get(char, 0) + 1

        for char in t:
            if char not in char_map or char_map[char] == 0:
                return False
            char_map[char] -= 1

        return True
        