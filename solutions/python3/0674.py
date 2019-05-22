class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0

        j = 0
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] >= nums[i]:
                j = i
            ans = max(ans, i - j + 1)

        return ans
