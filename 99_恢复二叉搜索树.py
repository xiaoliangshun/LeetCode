# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        #方法一是显式地将中序遍历的值序列保存在一个list1数组中，然后再去寻找被错误交换的节点，
        # 但我们也可以隐式地在中序遍历的过程就找到被错误交换的节点 x 和 y（用栈）

        def bianli(root):
            if root == None:
                return None
            bianli(root.left)
            list1.append(root)              #放的是结点
            bianli(root.right)
            return list1

        list1 = list()
        list1 = bianli(root)                #遍历一下

        x = -1;y = -1;flag = True           #要交换的两个位置的索引
        for i in range(1,len(list1)):               #####找到二叉搜索树中序遍历得到值序列的不满足条件的位置
            if list1[i-1].val > list1[i].val and flag:           #要修改
                x = i-1                 #第一个要换是前边的
                flag = False
            elif list1[i-1].val > list1[i].val and not flag:
                y = i                   #第二个要换是后边的
        if y == -1:             #表明要换两个是相邻的
            list1[x].val,list1[x+1].val = list1[x+1].val,list1[x].val
        else:                   #并不相连
            list1[x].val,list1[y].val = list1[y].val,list1[x].val

        return root
