# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    #DFS SOLUTION
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans=[]
        d={}
        def dfs(root,level):
            if root is None:
                return
            if level not in d:
                d[level]=root
            right=dfs(root.right,level+1)
            left=dfs(root.left,level+1)
        dfs(root,0)
        for i in sorted(d):
            ans.append(d[i].val)
        return ans
    #MORE OPTIMIZED:
    
    
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth+1)
                collect(node.left, depth+1)
            
        view = []
        collect(root, 0)
        return view
