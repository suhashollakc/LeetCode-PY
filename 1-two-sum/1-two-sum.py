class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#       Two-Pass Hash Table 
#         hashMap = {} #This holds the value and index
#         for i in range(len(nums)): #for each element
#             hashMap[nums[i]] = i #Add the key:value pair to hashmap
#         for i in range(len(nums)):
#             complement = target - nums[i]; #Calculating complement by subtracting target with current element
#             if complement in hashMap and hashMap[complement] != i:
#                 return [hashMap[complement],i]
            
#         One-Pass Hash Table
        hashMap = {} #This holds the value and index
        for i in range(len(nums)): #for each element
            complement = target - nums[i]
            if complement in hashMap:
                return [i,hashMap[complement]]
            hashMap[nums[i]] = i