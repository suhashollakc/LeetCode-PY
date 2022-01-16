class Solution:
    def isPalindrome(self, s: str) -> bool:
          s_al = []
          for char in s:
            if char.isalnum():
              s_al += char.lower()
          return s_al == s_al[::-1]