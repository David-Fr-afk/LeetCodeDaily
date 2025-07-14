class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(c.lower() for c in s if c.isalnum())
        i = 0
        j = len(s) - 1 
        while i < j:
            front_of_string = s[i]
            back_of_string = s[j]
            if front_of_string != back_of_string:
                return False
            i += 1
            j -= 1
        return True
    ##Above was the solution i created probably could have made it faster, cause in the beginning i made a whole new string so that the while loop could be cleaner. I think its worth the sacrifice.
        