# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:          ##迭代法
        prev = None
        curr = head
        while curr:
            next = curr.next            #next记录下一个节点
            curr.next = prev                #指向上一个节点
            prev = curr             #更新
            curr = next             #更新
        return prev
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:      #递归法
        if head == null or head.next == null:    #出口
            return head
        newHead = reverseList(head.next)        #递归
        head.next.next = head           #后边已经逆转的链表的最后一个节点指向该节点（实现逆转）
        head.next = null
        return newHead
