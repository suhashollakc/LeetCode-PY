from heapq import heapify, heappop, heappush
from typing import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)  #Hashmap, count each char
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        
        heapify(maxHeap) #O(n)
        
        prev = None
        res = ''
        
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            #most frequent char,e xcept prev
            
            cnt, char = heappop(maxHeap)
            
            res += char
            cnt += 1
            
            if prev :
                heappush(maxHeap,prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return res