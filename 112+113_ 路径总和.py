class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    ################################################3  112. 路径总和
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:         #基于队列的广度优先
        if not root:
            return False
        que_node = collections.deque([root])                #每层的节点
        que_val = collections.deque([root.val])             #对应上边队列，该元素从根节点开始的路径之和
        while que_node:
            now = que_node.popleft()
            temp = que_val.popleft()
            if not now.left and not now.right:          #为根节点
                if temp == sum:
                    return True
                continue                #进入下一次循环
            if now.left:                        #非根节点
                que_node.append(now.left)
                que_val.append(now.left.val + temp)
            if now.right:
                que_node.append(now.right)
                que_val.append(now.right.val + temp)
        return False

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:             ##递归
        if not root:                    ##有分支就是False，(即不允许到不是叶节点，即只有一个孩子的话不能到那个空的一边)
            return False
        if not root.left and not root.right:            ##只有到叶子节点的才行
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


####################################################    113. 路径总和 II
                    #我觉得用栈处理更好，当到叶节点时，判断栈内的总和

class Solution:
    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:               ###递归回溯
        ret = list()
        path = list()

        def dfs(root: TreeNode, total: int):
            if not root:
                return
            path.append(root.val)
            total -= root.val           #实践
            if not root.left and not root.right and total == 0:                 ##是叶节点且成立
                ret.append(path[:])                     #path[:]这样处理不会使得ret随着path而变化
            dfs(root.left, total)
            dfs(root.right, total)
            path.pop()                  #回溯

        dfs(root, total)
        return ret

class Solution:
    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:               ##广度优先搜索
        ret = list()
        parent = collections.defaultdict(lambda: None)

        def getPath(node: TreeNode):
            tmp = list()
            while node:
                tmp.append(node.val)
                node = parent[node]
            ret.append(tmp[::-1])

        if not root:
            return ret

        que_node = collections.deque([root])
        que_total = collections.deque([0])

        while que_node:
            node = que_node.popleft()
            rec = que_total.popleft() + node.val

            if not node.left and not node.right:
                if rec == total:
                    getPath(node)
            else:
                if node.left:
                    parent[node.left] = node
                    que_node.append(node.left)
                    que_total.append(rec)
                if node.right:
                    parent[node.right] = node
                    que_node.append(node.right)
                    que_total.append(rec)

        return ret




