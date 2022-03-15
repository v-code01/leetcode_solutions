class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        L = [''] * numRows
        index, step = 0, 1
        
        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(L)
   '''
   Explanation:
   Create a set of empty strings
   add index and step as the default variables
   add the letter to the string and then check to see the direction and adjust step according to that
   return joined zig zag
   '''
