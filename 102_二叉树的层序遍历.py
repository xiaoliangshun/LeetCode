class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def levelOrder(self, root):                   ###我写的法1
    #     list1 = list()              #使用的数组
    #     list3 = list()              #最终数组
    #     list1.append(root)
    #     while len(list1) != 0:
    #         list2 = list()              #每一层的数组
    #         leng = len(list1)               #该层的元素个数
    #         i = 0
    #         while i < leng:
    #             list2.append(list1[0].val)                  #通不过leetcode？？？？？？？
    #             root = list1[0]
    #             if root.left != None:
    #                 list1.append(root.left)
    #             if root.right != None:
    #                 list1.append(root.right)
    #             list1.remove(list1[0])
    #             i += 1
    #         list2_copy = list2.copy()
    #         list3.append(list2_copy)
    #     return list3


    # import collections
    # def levelOrder2(self, root):            #使用递归实现       #我的法2
    #     ans = collections.defaultdict(list)
    #     def leverl(root,lever):
    #         if root == None:
    #             return
    #         if root.left != None:
    #             ans[str(lever)] += [root.val]
    #             lever(root.left,lever+1)
    #         if root.right != None:
    #             ans[str(lever)] += [root.val]
    #             lever(root.right,lever+1)
    #     leverl(root,0)
    #     return ans

    def levelOrder3(self, root):            #使用队列实现     #别人的法1
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            temp = []
            l = len(queue)
            for i in range(l):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(temp)
        return ans

    ########法2：使用递归实现（标记每一个节点的层数），将其加入相应的某行             别人的法2
    def levelOrder4(self, root: TreeNode) -> List[List[int]]:
        d = collections.defaultdict(list)           #好用的字典

        def f(r, i):
            if r:
                d[i].append(r.val)
                f(r.left, i + 1)
                f(r.right, i + 1)

        f(root, 0)
        return [*d.values()]            #只取值（*可能表示全部）

root1 = TreeNode(3)
root2 = TreeNode(4)
root = TreeNode(2)
root.left = root1
root.right = root2

print(Solution().levelOrder1(root))