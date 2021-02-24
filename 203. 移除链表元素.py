# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        hh = ListNode(0,head)             ##创建头节点，将处理头节点的情况和后边的统一起来
        hhh = hh
        while hhh.next:
            if hhh.next.val == val:          #hh表示前边的节点，hh.next是工作节点
                hhh.next = hhh.next.next
            # print(hhh.val)
            else:
                hhh = hhh.next          #在删除了某节点时不需要移动指针
        return hh.next
print(Solution().isHappy(2))