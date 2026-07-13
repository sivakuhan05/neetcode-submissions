class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix, suffix = [1 for _ in range(length)], [1 for _ in range(length)]

        for i in range(1, length):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(length - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        res = []

        for i in range(length):
            res.append(prefix[i] * suffix[i])

        return res
