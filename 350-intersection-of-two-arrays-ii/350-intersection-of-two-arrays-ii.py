class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
       #Will be stored in the hash table for shorter elements
        #Ensure that the previous array is short
        if len(nums1) > len(nums2):
            self.intersect(nums2, nums1)
        
        hash_map = {}

        for num in nums1:
            if num not in hash_map:
                hash_map[num] = 0
            hash_map[num] += 1
        
        ans = []

        for num in nums2:
            #See if it exists in the hash table
            count = hash_map.get(num, 0)
            #If the element exists in the hash table, it is added to the result list
            #Then the number of occurrences of the elements corresponding to the hash table is reduced by one
            if count > 0:
                ans.append(num)
                hash_map[num]-=1
        
        return ans

        