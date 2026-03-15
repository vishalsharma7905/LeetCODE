class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        from collections import Counter
        
        need = Counter(c.lower() for c in licensePlate if c.isalpha())
        
        ans = None
        
        for word in words:
            count = Counter(word.lower())
            
            if all(count[c] >= need[c] for c in need):
                if ans is None or len(word) < len(ans):
                    ans = word
        
        return ans