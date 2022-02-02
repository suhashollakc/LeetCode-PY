class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # csum = 0
        # result = 0
        # for i in range(1,n+1):
        #     csum += i-1
        #     if csum >= n:
        #         break
        #     if (n - csum) % i == 0:
        #         result +=1
        # return result
        
        # intuition
        
        # eqn -> 4 + 5+ 6 = 15 can be simplified as (3 + 1) + (3 + 2) + (3+3) = 15
        # or 3 + 3 + 3 = 15 - 1- 2 -3
        # so 3 is base here and the RHS is also divisible by 3
        # If RHS is divisible by BASE = there is a consecutive sum
        count = 0
        i = 1
        while (n > 0):
            n -= i
            if n % i == 0:
                count += 1
            i += 1
        return count