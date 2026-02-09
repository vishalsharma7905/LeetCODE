from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(t) - Counter(s)
        return list(c.keys())[0]
