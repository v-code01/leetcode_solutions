class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag = set()
        inv_diag = set()
        current_result = []
        ans = []
        
        def make_output(answers):
            output = []
            
            for answer in answers:
                output.append([("." * col + "Q") + ("." * (n - col - 1))
                               for col in answer])
            return output
        
        def dfs(i):
            
            if len(current_result) == n:
                ans.append(current_result.copy())
                
            # iterate through each column
            for j in range(n):
                if (j not in cols 
                    and j - i not in diag
                    and j + i not in inv_diag):
                    current_result.append(j)
                    
                    cols.add(j)
                    diag.add(j - i)
                    inv_diag.add(j + i)
                    
                    dfs(i + 1)
                    current_result.pop()
                    cols.remove(j)
                    diag.remove(j - i)
                    inv_diag.remove(j + i)
        dfs(0)
        return make_output(ans)
      #49 MINS :)
