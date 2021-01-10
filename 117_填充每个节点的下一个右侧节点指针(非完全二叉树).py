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


    ########################################不使用队列                   我的代码：有毛病！！！
    def connect(self, root: 'Node') -> 'Node':

        def find(root):  # 找到下层的第一个节点
            while root:
                if root.left:
                    return root.left
                if root.right:
                    return root.right
                root = root.next
            return None

        def con(head):  ##将head所在层的下层节点串联在一起
            head_next = find(head)
            while head_next:
                root = head  # 保留最左节点
                while head:
                    if head.left and head.right:  # 左右子树都存在
                        head.left.next = head.right

                    if head.next:
                        if head.right:  # 有右孩子
                            if head.next.left:
                                head.right.next = head.next.left
                            if not head.next.left and head.right:
                                head.right.next = head.next.right
                        elif head.left and not head.right:  # 有左孩子，无右孩子
                            if head.next.left:
                                head.left.next = head.next.left
                            elif not head.next.left and head.right:
                                head.left.next = head.next.right
                    head = head.next
                head_next = find(root)  # 继续向下寻找
                head = head_next  # 更新

        con(root)
        return root


# class Solution {                                                  ###java代码
#     Node last = null, nextStart = null;
#
#     public Node connect(Node root) {
#         if (root == null) {
#             return null;
#         }
#         Node start = root;
#         while (start != null) {
#             last = null;                              ##保持为上一个待链接的节点
#             nextStart = null;                             ##下一层开始
#             for (Node p = start; p != null; p = p.next) {
#                 if (p.left != null) {
#                     handle(p.left);
#                 }
#                 if (p.right != null) {
#                     handle(p.right);
#                 }
#             }
#             start = nextStart;
#         }
#         return root;
#     }
#
#     public void handle(Node p) {
#         if (last != null) {
#             last.next = p;
#         }
#         if (nextStart == null) {
#             nextStart = p;
#         }
#         last = p;
#     }
# }




