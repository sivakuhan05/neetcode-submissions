class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { ')' : '(', '}' : '{', ']' : '['}

        for bracket in s:
            if stack and bracket in pairs:
                if stack[-1] == pairs[bracket]:
                    stack.pop()
                
                else:
                    return False
            
            else:
                stack.append(bracket)

        return True if not stack else False