# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:                             #None表示空对象   与Null空状态   不一样
    def zigzagLevelOrder(self, root):
        if root == None:                                #最后一个测试没过去
            return None
        list1 = []  ##层序遍历使用的队列
        list2 = []  ##每一层结果
        list3 = []  ##最终的结果
        list1.append(root)
        x = 1  # 判断是第奇数行还是偶数行
        while (list1):
            for i in range(len(list1)):  ##一层一层来
                root1 = list1[0]
                list1.pop(0)
                # print(type(root1))            #查看类型
                list2.append(root1.val)
                if root1.left:
                    list1.append(root1.left)
                if root1.right:
                    list1.append(root1.right)
            if x % 2 == 0:  ##我们默认从1开始，那莫偶数行逆序
                leng = len(list2)
                for i in range(leng // 2):
                    list2[i], list2[leng - 1 - i] = list2[leng - 1 - i], list2[i]  # 逆序添加
            list3.append(list2)
            list2 = []
            x += 1
        return list3
root = TreeNode(3)
root1 = TreeNode(9)
root2 = TreeNode(20)
root3 = TreeNode(15)
root4 = TreeNode(7)
root.left = root1
root.right = root2
root2.left = root3
root2.right = root4
root5 = []
print(Solution().zigzagLevelOrder(root))