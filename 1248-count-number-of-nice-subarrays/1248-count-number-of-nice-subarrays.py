class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #Let zeroeth odd index be -1
        #This way we can easily calculate the no of even number sbefore the first odd number using the same
        #way as between two odd numbers
        odd_indices =[-1]
        
        for i, entry in enumerate(nums):
            if entry % 2 == 1:
                odd_indices.append(i)
        if len(odd_indices) <= k:
            return 0
        
        ans = 0
        
        #For the same reason as above, the final index is n, where n is the size of nums
        
        odd_indices.append(len(nums))
        for i in range(len(odd_indices) - k - 1):
            start_diff = odd_indices[i+1] - odd_indices[i]
            end_diff = odd_indices[i+k+1] - odd_indices[i+k]
            ans += start_diff * end_diff
        return ans