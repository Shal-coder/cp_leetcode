class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for k, num in enumerate(nums):
            complement = target - num
            if complement in n:
                return [n[complement], k]
            n[num] = k
        return []
nums = [2,7,11,15]
target = 9
output = Solution().twoSum(nums,target)
print(output)
        