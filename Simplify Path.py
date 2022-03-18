class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for i in path.split('/'):
            if i in ('', '.'):
                pass
            elif i == '..':
                if stack: stack.pop()
            else:
                stack.append(i)
        return '/' + '/'.join(stack)
'''
using stack and cleaned up the first solution which assigned variables to everything and keeping list static slows it down.
'''
