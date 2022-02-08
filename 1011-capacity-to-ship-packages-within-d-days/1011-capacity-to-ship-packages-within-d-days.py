
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
    
        def feasible(capacity):
            days = 1
            local = 0
            for w in weights:
                local+=w
                if local>capacity:
                    local = w
                    days+=1
                    if days>D:
                        return False
            return True
            
                
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right-left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
            
        return left