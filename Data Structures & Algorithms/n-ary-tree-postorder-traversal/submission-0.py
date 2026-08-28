"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        def postorder(nods):
            if not nods:
                  return

            for i in nods.children:
                
                postorder(i)
            res.append(nods.val)
        postorder(root)
        return res