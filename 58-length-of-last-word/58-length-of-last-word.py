class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s = s.strip()
        # inp = list(s.split(" "))
        # return len(inp[-1])
        i = len(s) - 1
        
        while i >= 0 and s[i] == ' ':
            i -= 1
        lastIndex = i
        while i >= 0 and s[i] != ' ':
            i -= 1
        return lastIndex - i
        