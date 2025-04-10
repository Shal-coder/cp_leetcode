class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]
x = 121
result = Solution().isPalindrome(x)
print(result)
      
        