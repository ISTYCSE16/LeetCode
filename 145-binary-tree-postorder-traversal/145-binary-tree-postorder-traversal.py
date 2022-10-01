# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.ans.append(root.val)
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.postorder(root)
        return self.ans