# class Solution:
#     def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
#         nums.sort()
#         max_subsets = []
#         for i,num in enumerate(nums):
#             max_subset = 0
#             for j in range(i):
#                 if num% nums[j] == 0:
#                     max_subset = max(max_subset, max_subsets[j])
#             max_subsets.append(max_subset + 1)
        
#         return max(max_subsets)
    
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        res = [[num] for num in nums]  #contains sets starting with that number
        
        for i in range(n):
            for j in range(i):
                if (nums[i] % nums[j]) == 0 and len(res[i]) < len(res[j]) + 1:  #to ensure the length of the set is maximal 
                    res[i] = res[j] + [nums[i]]
                    
        return max(res, key=len)  #return max length set