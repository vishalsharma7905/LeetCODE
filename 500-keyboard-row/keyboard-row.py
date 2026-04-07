class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        ans = []
        
        for word in words:
            s = set(word.lower())
            
            if s <= row1 or s <= row2 or s <= row3:
                ans.append(word)
        
        return ans