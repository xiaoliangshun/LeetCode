class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        list1 = list()
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            list1.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(len(list1)-1):
            if list1[i] >= list1[i+1]:
                return False
        return True

    ###法2：我们可以设计一个函数 helper(node, lower, upper) 上下界，判断当前节点是否在区间内，
    #       递归对左子树  helper(node.left, node.val, upper)
    #       递归对右子树  helper(node.right, lower, node.val)