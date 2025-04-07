"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true


"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        for i in s:
            if i in par.keys():
                stack.append(i)
            elif i in par.values(): 
                if not stack:
                    return False
                end = stack.pop()
                if par[end] != i:
                    return False

        return len(stack) == 0
                
validador = Solution()
# s = "()"
# s = "()[]{}"
# s = "(]"
s = "([])"
print(validador.isValid(s))
    