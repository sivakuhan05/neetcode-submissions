class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for i in strs:
            res += str(len(i)) + "#" + i

        return res    
    
    def decode(self, s: str) -> List[str]:
        strs = []
        length = len(s)
        i = 0

        while i < length:
            j = i + 1
            
            while s[j] != "#":
                j += 1

            word_len = int(s[i: j])
            strs.append(s[j + 1: j + 1 + word_len])
            i = j + word_len + 1

        return strs


