class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        k = set()
        if len(set(nums)) != len(nums):
            return True
        else:
            return False
sol = Solution()
output=sol.containsDuplicate([1,2,3,1])
print(output)
        