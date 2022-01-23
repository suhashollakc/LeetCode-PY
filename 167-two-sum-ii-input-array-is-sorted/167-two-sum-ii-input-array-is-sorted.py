class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in hashMap and hashMap[complement] != i:
                if i > hashMap[complement]:
                    return [hashMap[complement]+1,i+1]
                else:
                    return [i+1, hashMap[complement]+1]
                
            hashMap[numbers[i]] = i