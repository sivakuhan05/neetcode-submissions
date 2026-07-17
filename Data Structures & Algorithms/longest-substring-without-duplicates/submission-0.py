class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        duplicate_check = set()
        length = len(s)
        l, r = 0, 0
        max_len = 0

        while r < length:
            
            if s[r] in duplicate_check:

                while s[l] != s[r]:
                    duplicate_check.remove(s[l])
                    l += 1

                l += 1
                r += 1
            
            else:
                duplicate_check.add(s[r])
                r += 1
            
            max_len = max(max_len, r - l)

        return max_len