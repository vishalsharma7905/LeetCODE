class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--.."
        ]
        
        st = set()
        
        for word in words:
            code = ""
            
            for ch in word:
                code += morse[ord(ch) - ord('a')]
            
            st.add(code)
        
        return len(st)