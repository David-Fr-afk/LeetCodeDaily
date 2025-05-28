class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        if strs: 
            for words in strs:
                key = ''.join(sorted(words))
                if key not in anagrams:
                    anagrams[key] = []
                anagrams[key].append(words)
            return list(anagrams.values())
        else:
            return []
#this one wasnt too bad, I did struggle with truly understanding how maps work and how sorted() words, but i figured it out and thought this problem was fun.

        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        