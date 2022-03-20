class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # I have two solutions approach for this. One,
        #Making an hash table and storing the elements with indexes and checking if the 
        #complement is in the hashmap, if it is, we found the numbers, complement and hashmap key
        
        #Another one is assuming, the array is not sorted or any criteria regarding it,
        #I will sort the array, then check the sum of two elements using no extra space
        #and if sum matches the targetSum, we found the answer.
        
        #Approach 1. using hashmap
        
        hashMap = {}
        
        for value in range(len(nums)):
            hashMap[nums[value]] = value
        
        for i in range(len(nums)):
            
            complement = target - nums[i]
            
            if complement in hashMap and hashMap[complement] != i:
                return [i,hashMap[complement]]