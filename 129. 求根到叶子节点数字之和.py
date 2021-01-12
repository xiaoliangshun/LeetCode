class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:            ###先序遍历
        def preOrder(root,sum_1):
            if not root:                ##为空时，先行退出
                return 0
            sum_1 += root.val
            if not root.left and not root.right:        #为叶子节点
                return sum_1                    #不再使用全局变量
            return preOrder(root.left,sum_1*10) + preOrder(root.right,sum_1*10)
        return preOrder(root,0)

    def sumNumbers1(self, root: TreeNode) -> int:            ####与上边方法一样
        def dfs(root: TreeNode, prevTotal: int) -> int:
            if not root:
                return 0
            total = prevTotal * 10 + root.val
            if not root.left and not root.right:
                return total
            else:
                return dfs(root.left, total) + dfs(root.right, total)

        return dfs(root, 0)

################ 使用广度优先搜索，需要维护两个队列，分别存储节点和节点对应的数字。
    def sumNumbers2(self, root: TreeNode) -> int:
        if not root:
            return 0

        total = 0
        nodeQueue = collections.deque([root])
        numQueue = collections.deque([root.val])

        while nodeQueue:
            node = nodeQueue.popleft()          #出栈
            num = numQueue.popleft()
            left, right = node.left, node.right
            if not left and not right:
                total += num
            else:
                if left:
                    nodeQueue.append(left)      #入栈
                    numQueue.append(num * 10 + left.val)
                if right:
                    nodeQueue.append(right)
                    numQueue.append(num * 10 + right.val)

        return total

