class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used = set() # Character in t already used as value in mapping
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            a_char = s[i]
            b_char = t[i]
            if a_char in mapping:
                if mapping[a_char] != b_char:
                    return False
            else:
                if b_char in used:
                    return False
                mapping[a_char] = b_char
                used.add(b_char)
        return True
        