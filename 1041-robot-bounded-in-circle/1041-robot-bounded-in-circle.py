class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y,dx,dy = 0,0,0,1
        
        for move in instructions:
            if move == 'G':
                x,y = x+dx, y+dy
            elif move == 'R':
                dx,dy = dy, -dx
            else:
                dx,dy = -dy, dx
        return (x,y) == (0,0) or (dx,dy) != (0,1)