class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        #using hashmap and keeping count of all the charatcers. TC-> O(N), SC -> O(1)  (Linear Time Solution)
#         count = collections.Counter(s)
        
#         for idx, ch in enumerate(s):
#             if count[ch] == 1:
#                 return idx
#         return -1
    
    #You can also do a set soulution
        duplicates = set()
        for i in range(len(s)):
            if s[i] in duplicates:
                continue
            if s[i] not in s[i+1:]:
                return i
            duplicates.add(s[i])
        return -1