class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        final = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            if c == ")":
                if len(stack) != 1:
                    start = stack.pop()
                    length = (i - stack[-1])
                    longest_length = max(length,final)
                else:
                    stack.pop()
                    stack.append(i)
        return final
