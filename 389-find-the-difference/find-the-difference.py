class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for ch in s:
            res ^= ord(ch)
        for ch in t:
            res ^= ord(ch)
        return chr(res)
