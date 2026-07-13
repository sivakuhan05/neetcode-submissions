class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = min(len(nums), 1)

        for i in nums:
            temp = i

            if (temp - 1) not in nums_set:
                count = 1
                
                while temp + 1 in nums_set:
                    temp += 1
                    count += 1

                if count > max_count:
                    max_count = count

        return max_count