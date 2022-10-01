'''
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
'''

class Solution:
    
    def traverse(self, root):
        if root:
            for child in root.children:
                self.traverse(child)
            self.ans.append(root.val)
    
    def postorder(self, root: 'Node') -> List[int]:
        self.ans = []
        self.traverse(root)
        return self.ans