class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = -1
        right = -1

        max_seen = float("-inf")
        for i in range(n):
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                right = i

        if right == -1:
            return 0

        min_seen = float("inf")
        for i in range(n - 1, -1, -1):
            min_seen = min(min_seen, nums[i])
            if nums[i] > min_seen:
                left = i

        return right - left + 1