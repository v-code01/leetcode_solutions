class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {'2': ['a','b','c'],
                   '3': ['d','e','f'],
                   '4': ['g','h','i'],
                   '5': ['j','k','l'],
                   '6': ['m','n','o'],
                   '7': ['p','q','r', 's'],
                   '8': ['t','u','v'],
                   '9': ['w','x','y', 'z']}
        ans = []
        def dfs(digits, current_path):
            if not digits:
                ans.append(current_path)
            else:
                for letter in mapping[digits[0]]:
                    dfs(digits[1:], current_path + letter)
        dfs(digits, "")
        return ans
      
      #FASTEST SOLUTION 
