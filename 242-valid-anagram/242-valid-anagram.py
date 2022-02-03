class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterDictionary = {}
        
        for char in s:
            if char not in letterDictionary:
                letterDictionary[char] = 1
            else:
                letterDictionary[char] += 1
                
        for char in t:
            if char not in letterDictionary:
                return False
            else:
                if letterDictionary[char] == 1:
                    del letterDictionary[char]
                    
                else:
                    letterDictionary[char] -= 1
        
        if letterDictionary != {}:
            return False
        return True
        