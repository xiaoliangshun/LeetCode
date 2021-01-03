# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:             ##DFS，，也可以使用队列实现BFS
        def isSame(p,q):
            if p == None and q == None:         #都是空
                return True
            elif p == None or q == None:         #其一为空
                return False
            elif p.val == q.val:                                   #皆不为空--相等
                return isSame(p.left,q.left) and isSame(p.right,q.right)
            else:                                                     #皆不为空--不相等
                return False
        return isSame(p,q)