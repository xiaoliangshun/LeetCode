class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
      self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:      #关键点在意左/右子树为空时，要选择有高度的一边；；左右都存在时为高度的较小值
        def minD(root):
            if not root:                        #空
                return 0
            elif not root.left and root.right:      #只有左孩子
                return minD(root.right) + 1
            elif not root.right and root.left:          #只有右孩子
                return minD(root.left) + 1
            else:
                return min(minD(root.left),minD(root.right)) + 1
        return minD(root)

    def minDepth2(self, root: TreeNode) -> int:         ####官方答案
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        min_depth = 10 ** 9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)           #如果存在左，就对比左右的最小值

        return min_depth + 1


        #方法2：用层序遍历也不错，使用step计数，出队时判断当前节点是否有左右孩子，:
    class Solution:
        def minDepth(self, root: TreeNode) -> int:
            if not root:
                return 0

            que = collections.deque([(root, 1)])
            while que:
                node, depth = que.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    que.append((node.left, depth + 1))
                if node.right:
                    que.append((node.right, depth + 1))

            return 0
