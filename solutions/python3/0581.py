class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        _min = float('inf')
        _max = float('-inf')
        flag = False

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                flag = True
            if flag:
                _min = min(_min, nums[i])

        flag = False

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                flag = True
            if flag:
                _max = max(_max, nums[i])

        for l in range(len(nums)):
            if nums[l] > _min:
                break

        for r in range(len(nums) - 1, -1, -1):
            if nums[r] < _max:
                break

        return 0 if r - l <= 0 else r - l + 1
