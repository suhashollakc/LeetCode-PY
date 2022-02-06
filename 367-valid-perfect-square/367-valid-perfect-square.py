class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        #Recursion - Slowest one
        #Binary Search - The Simplest One
        # Newton's Method - The fastest one, and therefore widely used in dynamic simulations.
        
        # Binary Search Approach
        # For num > 2 , the square root a is always less than num/2 and greater than 1: 1 < x < num/2
        #Algorithm
        # if num < 2, return True
        # Set left boundary to 2, and right boundary to num/2
        # While left <= right:
        # Take x = (left+right)/2 as a guess. Compute guess_squared = x*x and compare it with num:
        # IF guess_squared == num, then the perfect square is found, return True
        # If guess_Squared > num, move the right boundary right.... right = x- 1
        # Otherwise, move the left boundary left = x+1
        
        # If not found, return False
        
        # Time COmplexity : O(logN)
        # Space COmplexity: O(1)
        if num < 2:
            return True
        
        left,right = 2, num//2
        
        while left <= right:
            x = left + (right-left)//2
            guess_squared = x*x
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = x-1
            else:
                left = x + 1
            
        return False
