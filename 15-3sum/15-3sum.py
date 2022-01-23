class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSumII(nums,i,res)
        return res
    
    def twoSumII(self,nums:List[int],i:int,res:List[List[int]]):
        lo,hi = i+1 ,len(nums)-1
        while (lo < hi):
            sum = nums[i]+nums[lo]+nums[hi]
            if sum < 0:
                lo+=1
            elif sum > 0:
                hi -=1
            else:
                res.append([nums[i],nums[lo],nums[hi]])
                lo +=1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1
                    
        
        
        
        
        
        
        # Other Variant
#         nums.sort()
#         ans = []
#         N = len(nums)
        
#         for i in range(N):
#             j = i+1
#             k = N-1
            
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
                
#             while j < k:
#                 s = nums[i] + nums[j] + nums[k]
                
#                 if s > 0:
#                     k  -=1
#                 elif s < 0:
#                     j +=1
#                 else:
#                     ans.append([nums[i],nums[j],nums[k]])
                    
#                     while j < k and nums[k] == nums[k-1]: k-=1
#                     while j < k and nums[j]==nums[j+1]: j+=1
#                     k -= 1
#                     j += 1
#         return ans
                    