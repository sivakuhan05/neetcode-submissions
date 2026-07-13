class Solution:

    def encode(self, strs: List[str]) -> str:
        length = len(strs)

        for i in range(length):
            strs[i] = str(len(strs[i])) + "#" + strs[i]

        string = ""
        for i in strs:
            string += i

        return string
    
    
    def decode(self, s: str) -> List[str]:
        strs = []
        length = len(s)
        i = 0

        while i < length:
            j = i + 1
            
            while s[j] != "#":
                j += 1

            word_len = int(s[i: j])
            word = s[j + 1: j + 1 + word_len]
            strs.append(word)
            i = j + word_len + 1

        return strs


