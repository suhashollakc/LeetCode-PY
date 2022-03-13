from heapq import heappop,heappush
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        #keep track of items in the heap, and their row and column numbers
        heap = [(matrix[0][0],0,0)]
        #keep track of the top of each row that is not processed
        column_top = [0]*n
        #keep track of the first number each row not processed
        row_first = [0]*n
        #Repeat the process k -1 times
        while k > 1:
            k -= 1
            min_val, row, column = heappop(heap)
            row_first[row] = column + 1
            #Add the item on the righ to the heap if everything above it is processed
            if column + 1 < n and column_top[column+1] == row:
                heappush(heap,(matrix[row][column+1],row,column+1))
            column_top[column] = row + 1
            #Add the item below it to the heap if everything before it is procesed
            
            if row + 1 < n and row_first[row+1] == column:
                heappush(heap,(matrix[row+1][column],row+1,column))
        return heap[0][0]