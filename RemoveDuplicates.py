class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for n in range(len(nums)):
            if nums[n] != nums[k]:
                k += 1
                nums[k] = nums[n]
        return k + 1
        if not nums:
            return 0
s = Solution()
output=s.removeDuplicates([1,1,2,1])
print(output)
        