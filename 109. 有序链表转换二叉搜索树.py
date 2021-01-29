# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:         ####我的：有问题？？
        def soetedList(head):
            if not head :
                return
            leng = 0            #记录元素个数
            end = head
            while end.next != None:
                leng += 1
                end = end.next
            if leng == 1:           ##递归出口
                return TreeNode(head.val)

            mid = leng // 2
            head_1 = head
            for i in range(mid):
                head_1 = head_1.next            ##找到中间位置作为节点
            node1 = TreeNode(head_1.val)           ##创建节点 ,head_1是中间节点   ？？？？？？？？？？？？？？
            head_2 = head_1.next
            head_1.next = None                      #截断
            node1.left = soetedList(head)
            node1.right = soetedList(head_2)
            return node1
        return soetedList(head)


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMedian(left: ListNode, right: ListNode) -> ListNode:     ##找到中间节点
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        def buildTree(left: ListNode, right: ListNode) -> TreeNode:             ##right其实表示最后元素的下一个空节点
            if left == right:
                return None
            mid = getMedian(left, right)
            root = TreeNode(mid.val)        #创建节点
            root.left = buildTree(left, mid)        #递归
            root.right = buildTree(mid.next, right)
            return root

        return buildTree(head, None)            #这里首次传入的None不是代表right为空，而是判断left是否为空，我们在建立树的过程中只是用到了开始的头节点

##方法二：分治 + 中序遍历优化
#因为二查搜索树的中序遍历刚好是一个递增序列，要保证是二叉平衡树，只用保证每个的跟都是中间节点就ok了
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getLength(head: ListNode) -> int:
            ret = 0
            while head:
                ret += 1
                head = head.next
            return ret

        def buildTree(left: int, right: int) -> TreeNode:           ##中序创建空节点，然后一个一个装
            if left > right:
                return None
            mid = (left + right + 1) // 2
            root = TreeNode()
            root.left = buildTree(left, mid - 1)
            nonlocal head           ##nonlocal声明的变量只对局部起作用，离开封装函数，那么该变量就无效。
            root.val = head.val
            head = head.next
            root.right = buildTree(mid + 1, right)
            return root

        length = getLength(head)
        return buildTree(0, length - 1)
