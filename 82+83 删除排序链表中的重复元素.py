# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:                         ##83. 删除排序链表中的重复元素 I
        if head == None:
            return head
        head_1 = head       ##保持在第一个不同值的位置
        while head_1.next != None:
            if head_1.next.val == head_1.val:
                head_1.next = head_1.next.next

            else:
                head_1 = head_1.next
        return head

##########################  82. 删除排序链表中的重复元素 II

    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     if head == None:                                              ######????????有问题
    #         return head
    #     h = ListNode(8888)
    #     h.next = head               #头节点(上一个不重复的节点)
    #     work = head.next             #工作节点
    #     temp = work.val         #上一个相同元素的值
    #     hh = None
    #     flag = True
    #     while work != None:
    #         if work.val == temp:
    #             h.next = work.next
    #             work = h.next
    #
    #         else:
    #             if flag:            ##判断第一个节点
    #                 hh = work
    #             temp = work.val
    #             work = work.next
    #             h = h.next
    #     return hh
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:       #特殊情况:头节点为null或头节点下一节点为null，直接返回头节点，这时不存在重复节点
            return head
        if head.val == head.next.val:       #跳过所有相等节点。递归调用函数判断最后一个跳过节点的后一节点。
            while head != None and head.next != None and head.val == head.next.val:         #去除重复节点
                head = head.next
            return self.deleteDuplicates(head.next)         #这里的head.next是第一个与前边不重复的节点
        else:
            head.next = self.deleteDuplicates(head.next)            #指向下一个不重复的节点
            return head

print(Solution().deleteDuplicates())
