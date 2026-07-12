class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        array_length = len(strs)

        for i in range(array_length):
            count = [0 for _ in range(26)]
            
            for j in strs[i]:
                count[ord(j) - ord('a')] += 1 
            
            key = tuple(count)

            if key in hash:
                hash[key].append(strs[i])
            else:
                hash[key] = [strs[i]]

        result = []

        for key in hash:
            result.append(hash[key])

        return result