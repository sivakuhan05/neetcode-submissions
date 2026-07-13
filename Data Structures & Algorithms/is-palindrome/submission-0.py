class Solution:
    def isPalindrome(self, s: str) -> bool:
        comp_string = ""

        for i in s:
            if i.isalnum():
                comp_string += i
        
        length = len(comp_string)

        for i in range(length // 2):
            if comp_string[i].lower() != comp_string[length - i - 1].lower():
                return False

        return True