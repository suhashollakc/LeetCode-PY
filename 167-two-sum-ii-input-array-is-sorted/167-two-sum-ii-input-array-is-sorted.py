class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers)-1
        while True:
            sum = numbers[lo] + numbers[hi]
            if sum < target:
                lo += 1
            elif sum > target:
                hi -= 1
            else:
                return [lo+1, hi+1]
    
        
        
                #Two Pointer Approach Variant 2
#         low,high = 0,len(numbers)-1
#         while low < high:
#             sum = numbers[low]+numbers[high]
#             if sum == target:
#                 return [low+1,high+1]
#             elif sum < target:
#                 low+=1
#             else:
#                 high -= 1
#         return [-1,-1]
        
        
# One-Pass- Approach
#         hashMap = {}
#         for i in range(len(numbers)):
#             complement = target - numbers[i]
#             if complement in hashMap and hashMap[complement] != i:
#                 if i > hashMap[complement]:
#                     return [hashMap[complement]+1,i+1]
#                 else:
#                     return [i+1, hashMap[complement]+1]
                
#             hashMap[numbers[i]] = i


#Two Pointers Approach Variant 1
