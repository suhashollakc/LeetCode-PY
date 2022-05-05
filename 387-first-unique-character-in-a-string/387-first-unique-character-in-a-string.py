class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        #using hashmap and keeping count of all the charatcers. TC-> O(N), SC -> O(1)
        count = collections.Counter(s)
        
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1