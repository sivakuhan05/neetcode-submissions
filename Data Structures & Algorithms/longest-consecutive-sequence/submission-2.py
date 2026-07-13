class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = min(len(nums), 1)

        for i in nums:
            if (i - 1) not in nums_set:
                count = 1
                
                while i + 1 in nums_set:
                    i += 1
                    count += 1

                if count > max_count:
                    max_count = count

        return max_count