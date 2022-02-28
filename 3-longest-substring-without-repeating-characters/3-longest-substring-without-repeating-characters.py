class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #Sliding Window Problem
        l = r = 0
        window = set()
        n = len(s)
        longest = 0
        
        while r < n :
            if s[r] not in window:
                window.add(s[r])
                r += 1
            else:
                window.remove(s[l])
                l += 1
            longest = max(longest, r - l)
        return longest
                
#         charSet= set()
#         left = 0
#         result = 0
        
#         for right in range(len(s)):
#             while s[right] in charSet:
#                 charSet.remove(s[left])
#                 left +=1
#             charSet.add(s[right])
#             result = max(result, right - left + 1)
#         return result