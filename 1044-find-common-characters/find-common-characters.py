class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Step 1: count first word
        common = Counter(words[0])
        
        # Step 2: compare with rest
        for i in range(1, len(words)):
            current = Counter(words[i])
            
            for ch in common:
                common[ch] = min(common[ch], current[ch])
        
        # Step 3: build result
        result = []
        for ch in common:
            result.extend([ch] * common[ch])
        
        return result