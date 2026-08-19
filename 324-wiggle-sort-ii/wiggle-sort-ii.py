class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        median = sorted(nums)[n // 2]

        def vi(i):
            return (1 + 2 * i) % (n | 1)

        low, mid, high = 0, 0, n-1
        while mid <= high:
            if nums[vi(mid)] > median:
                nums[vi(low)], nums[vi(mid)] = nums[vi(mid)], nums[vi(low)]
                low += 1
                mid += 1
            elif nums[vi(mid)] < median:
                nums[vi(mid)], nums[vi(high)] = nums[vi(high)], nums[vi(mid)]
                high -= 1
            else:
                mid += 1

