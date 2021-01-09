class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':          ##队列的做法
        if not root:
            return None
        list1 = list()
        list1.append(root)
        while list1:
            leng = len(list1)
            for i in range(leng):
                root1 = list1.pop(0)  ##出队
                if i < leng - 1:  # 最后一个节点不用处理
                    root1.next = list1[0]

                if root1.left:  # 入队
                    list1.append(root1.left)
                if root1.right:
                    list1.append(root1.right)
        return root

            #########不使用队列
            #链接https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/solution/tian-chong-mei-ge-jie-dian-de-xia-yi-ge-you-ce-2-4/
    def connect(self, root: 'Node') -> 'Node':
        class Solution:
            def connect(self, root: 'Node') -> 'Node':
                if not root:
                    return root

                # 从根节点开始
                leftmost = root                     ###上层的最左节点

                while leftmost.left:            #题中是完全二叉树

                    # 遍历这一层节点组织成的链表，为下一层的节点更新 next 指针
                    head = leftmost
                    while head:             ##head为已经链接好的上一层

                        # CONNECTION 1    （同父）
                        head.left.next = head.right

                        # CONNECTION 2      （异父）
                        if head.next:
                            head.right.next = head.next.left

                        # 指针向后移动
                        head = head.next

                    # 去下一层的最左的节点
                    leftmost = leftmost.left            ##更新最左节点

                return root





