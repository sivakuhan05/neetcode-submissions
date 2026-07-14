class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        
        for i in range(length - 2):
            if i != 0 and nums[i - 1] == nums[i]:
                continue

            j = i + 1
            k = length - 1

            while j < k:
                
                if nums[j] + nums[k] == -nums[i]:
                    res.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1
                    
                    while j < length - 1 and nums[j - 1] == nums[j]:
                        j += 1

                    while k > i + 1 and nums[k + 1] == nums[k]:
                        k -= 1
                
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1

        return res
