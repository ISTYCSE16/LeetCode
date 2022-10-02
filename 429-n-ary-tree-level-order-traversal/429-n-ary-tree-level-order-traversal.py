"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
        
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if root:
            q = collections.deque([root])
            ans = []
            while q:
                temp = []
                size = len(q)
                for i in range(size):
                    node = q.popleft()
                    temp.append(node.val)
                    for child in node.children:
                        q.append(child)
                ans.append(temp)
            
            return ans
        
        