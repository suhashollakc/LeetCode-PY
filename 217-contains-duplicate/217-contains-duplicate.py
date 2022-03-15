from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #Make a hashset , with key -> num in nums and value -> Count(num).
        #If count(num) >=2 return true else False
        
        nums = Counter(nums)
        for key,val in nums.items():
            if val >= 2:
                return True
        return False
        
        