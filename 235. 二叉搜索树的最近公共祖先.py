# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    ##  两次遍历法
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findNode(node):
            list1 = list()
            while root:
                list1.append(root)              ##遍历并做记录
                if root.val == node.val:
                    return list1
                elif root.val < node.val:
                    root = root.right
                else:
                    root = root.left
        list1 = findNode(p)
        list2 = findNode(q)
        mostnear = root
        for i in range(min(len(list1),len(list2))):
            if list1[i] == list2[i]:            ##最近的一个出现在最后相同的地方
                mostnear = list1[i]
        return mostnear

    ##一次遍历法
    ##因为该树是一颗搜索树，p和q最新的祖先应该是在p、q中间（p、q分别在该节点的两端）
    #当节点值比p、q都大时往左后，
    #当节点值比p、q都小时往右后，
    #当节点值在p、q中间时，返回当前节点，
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        max1 = max(p.val, q.val)
        min1 = min(p.val, q.val)

        while True:
            if root.val > max1:
                root = root.right
            elif root.val < min1:
                root = root.left
            else:
                break
        return root