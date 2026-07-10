class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        for letter in s:
            hash1[letter] = hash1.get(letter, 0) + 1
        
        for letter in t:
            hash2[letter] = hash2.get(letter, 0) + 1

        return hash1 == hash2