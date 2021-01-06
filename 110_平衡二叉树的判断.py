class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:           ##自顶向下的递归，，先序
        def hight(root):                            #找出树高
            if not root:
                return 0
            return 1 + max(hight(root.left),hight(root.right))
        if not root:
            return True
        if abs(hight(root.left)-hight(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)           #递  归查找,但是从上往下查找的过程中存在重复

    def isBalanced(self, root: TreeNode) -> bool:               #自底向上的后续遍历
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:      #左右子树如果有一个不成立，或当前节点不行，一路往上传递
                return -1           #表示不平衡
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0
