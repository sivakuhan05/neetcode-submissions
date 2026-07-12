class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        freq = []

        length = len(nums)
        i = 0

        while i < length:
            j = i + 1

            while j < (length) and (nums[j] == nums[i]):
                j += 1
            
            freq.append((nums[i], j - i))
            i = j

        freq.sort(key = lambda x: x[1], reverse = True)

        return [freq[i][0] for i in range(k)]

        