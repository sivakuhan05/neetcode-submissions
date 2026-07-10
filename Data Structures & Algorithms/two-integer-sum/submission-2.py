class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        
        for i in nums:
            hash[i] = hash.get(i, 0) + 1

        length = len(nums)
        
        for i in range(length):
            difference = target - nums[i]
            
            if difference == nums[i]:
                if hash[nums[i]] > 1:
                    return [i, nums[i + 1:].index(difference) + i + 1]
            
            elif difference in hash:
                return [i, nums.index(difference)] 