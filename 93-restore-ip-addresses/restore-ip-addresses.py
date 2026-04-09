class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def backtrack(start, path):
            # If we have 4 parts
            if len(path) == 4:
                # If we used all characters
                if start == len(s):
                    res.append(".".join(path))
                return
            
            # Try 1, 2, 3 digits
            for length in range(1, 4):
                if start + length > len(s):
                    break
                
                part = s[start:start+length]
                
                # Check valid
                if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                    continue
                
                backtrack(start + length, path + [part])
        
        backtrack(0, [])
        return res