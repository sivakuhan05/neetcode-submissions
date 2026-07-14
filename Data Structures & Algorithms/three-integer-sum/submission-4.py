class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        
        for i in range(length - 2):
            if nums[i] > 0:
                break

            if i != 0  and nums[i - 1] == nums[i]:
                continue

            j = i + 1
            k = length - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum == 0:
                    res.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1
                    
                    while j < length - 1 and nums[j - 1] == nums[j]:
                        j += 1
                
                elif sum < 0:
                    j += 1
                
                elif sum > 0:
                    k -= 1

        return res
