class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ") #converting pattern to list
        frequency = {}  # dictionary to hold frequency of words   
        if len(pattern) != len(s): #checking lengths of pattern and the input s
            return False 
        elements = set() #set holding elements
        
        for i in range(len(pattern)):
            ch = pattern[i] 
            if ch in frequency:
                if frequency[ch]!=s[i]:
                    return False
            else:
                if s[i] not in elements:
                    frequency[ch] = s[i]
                    elements.add(s[i])
                else:
                    return False
        return True
        
        
        