# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:                     ####我的：：题目要求在原二叉树上调整（原地调整），这里又创建了一个二叉树（错的）
    def flatten(self, root: TreeNode) -> None:
        def preorder(root):
            if root == None:
                return None
            else:
                ROOT = TreeNode(root.val)
                ROOT.right = inorder(root.left)
                ROOT.right.right = inorder(root.right)              #有问题
            return ROOT

    ###letcode：迭代实现前序遍历(也可以使用递归)-->再对其进行合并
    def flatten2(self, root: TreeNode) -> None:
        preorderList = list()              #先序遍历结果的栈
        stack = list()                  #递归工作栈
        node = root

        while node or stack:
            while node:
                preorderList.append(node)
                stack.append(node)                  #记录顺序(要遍历的)
                node = node.left
            node = stack.pop()
            node = node.right

        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr

    ##   前序遍历和展开同步进行
    class Solution:
        def flatten(self, root: TreeNode) -> None:
            if not root:
                return

            stack = [root]
            prev = None

            while stack:
                curr = stack.pop()
                if prev:
                    prev.left = None
                    prev.right = curr
                left, right = curr.left, curr.right         #先序的关键（像是层序，但这里是栈--》先序）
                if right:                       #先右
                    stack.append(right)
                if left:                    #后左
                    stack.append(left)
                prev = curr

    ### 寻找前驱节点
    ##1.将当前节点的前驱（左子树最右节点）找到，将前驱节点的右子树指向当前节点的右孩子，当前节点的左子树变成右子树，这样一直往下找
    class Solution:
        def flatten(self, root: TreeNode) -> None:
            curr = root
            while curr:
                if curr.left:
                    predecessor = nxt = curr.left  
                    while predecessor.right:                #前驱
                        predecessor = predecessor.right
                    predecessor.right = curr.right
                    curr.left = None
                    curr.right = nxt
                curr = curr.right

print(Solution().)
