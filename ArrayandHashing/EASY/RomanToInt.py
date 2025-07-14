class Solution(object):
    def romanToInt(self, s):
        i = 0
        count = 0
        while i < len(s):
            if s[i] == 'I':
                if i + 1 < len(s) and s[i+1] in ('V', 'X'):
                    count -= 1
                else:
                    count += 1
            elif s[i] == 'V':
                count += 5
            elif s[i] == 'X':
                if i + 1 < len(s) and s[i+1] in ('L', 'C'):
                    count -= 10
                else:
                    count += 10
            elif s[i] == 'L':
                count += 50
            elif s[i] == 'C':
                if i + 1 < len(s) and s[i+1] in ('D', 'M'):
                    count -= 100
                else:
                    count += 100
            elif s[i] == 'D':
                count += 500
            else:  # s[i] == 'M'
                count += 1000
            i += 1
        return count

#Below I have attached the smarter method, which uses a map. I did this because I am not familiar with maps yet but I will get there.
'''
class Solution(object):
    def romanToInt(self, s):
        roman = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500,
            'M': 1000
        }
        
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                total += roman[s[i+1]] - roman[s[i]]
                i += 2  # Skip the next character as it's been processed
            else:
                total += roman[s[i]]
                i += 1
        return total
        '''