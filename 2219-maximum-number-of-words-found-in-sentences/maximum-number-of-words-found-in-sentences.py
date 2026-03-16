class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        
        for sentence in sentences:
            count = len(sentence.split())
            max_words = max(max_words, count)
            
        return max_words