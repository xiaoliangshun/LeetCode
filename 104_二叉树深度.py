# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:                         #递归出口          （DFS深度优先）
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1              #左右子树的较大值+1:表示当前层的最大深度

    def maxDepth2(self, root: TreeNode) -> int:         #队列方法 （BFS广度优先）
        if root is None:
            return 0
        queue = [(1, root)]                 #——————————————————--元组型数组
        while queue:
            depth, node = queue.pop(0)                      #每次出队，都会将下一层的孩子全都带进来
            if node.left:
                queue.append((depth + 1, node.left))
            if node.right:
                queue.append((depth + 1, node.right))
        return depth


