class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            word = s[start:end]
            res.append(word)
            i = end
        return res
