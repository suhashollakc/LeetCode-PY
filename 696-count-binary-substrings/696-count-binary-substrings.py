class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        #convert string s to array groups that represent length of same-character contiguous blocks within the string
        #ex : s: 11001100 , then groups = [2,2,2,2]
         
        groups = [1]
        
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1
                
        ans = 0
        
        for i in range(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans
                
                
                
        
        