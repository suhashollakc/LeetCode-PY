class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Problem Walk through
        #Approach 
        
        #1. Brute Force -> Loop through the array, check if array[i] + array[i+1] == target, if so return the index of the same
#         for i in range(len(nums)):
#             if nums[i] + nums[i+1] == target:
#                 return [i,i+1]
#         return []
        
        #2. Using Hashmap -> store the index as key and number as the value. Calculate the complement. if the complement in the hashmap and its not same as num, and num + complement == target, return the indices of both num and complement. else return none
        
        hashMap = {}
        
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap and hashMap[complement] != i:
                return [i, hashMap[complement]]
        return []

                
            