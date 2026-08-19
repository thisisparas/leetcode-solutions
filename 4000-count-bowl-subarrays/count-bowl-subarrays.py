class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        has_pge = [False] * n
        has_nge = [False] * n

        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            has_pge[i] = bool(stack)
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            has_nge[i] = bool(stack)
            stack.append(i)
        
        return sum(1 for i in range(n) if has_pge[i] and has_nge[i])