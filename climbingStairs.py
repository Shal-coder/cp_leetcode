class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        x, y = 1,2
        for i in range(2,n):
            x,y = y, x+y
        return y
sol = Solution()
n = 2
result = sol.climbStairs(n)
print(result)

        
        