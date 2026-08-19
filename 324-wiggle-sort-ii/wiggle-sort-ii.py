class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store], nums[i] = nums[i], nums[store]
                    store += 1
            nums[right], nums[store] = nums[store], nums[right]
            return store

        def find_median():
            left, right = 0, n - 1
            target = n // 2
            while True:
                pivot_index = random.randint(left, right)
                pivot_index = partition(left, right, pivot_index)
                if pivot_index == target:
                    return nums[pivot_index]
                elif pivot_index < target:
                    left = pivot_index + 1
                else:
                    right = pivot_index - 1

        median = find_median()

        def vi(i):
            return (1 + 2 * i) % (n | 1)

        low, mid, high = 0, 0, n - 1
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
