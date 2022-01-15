class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        inp = list(s.split(" "))
        return len(inp[-1])