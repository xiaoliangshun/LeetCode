# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
            ##将值复制到数组中后倒着对比
    def isPalindrome(self, head: ListNode) -> bool:         ##
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]

            ##快慢指针：1.找到后半部分的开始节点，2.将其反转然后与前半部分对比
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        list1 = list()
        while fast:             ##使用快慢指针定位中间位置
            list1.append(slow.val)
            slow = slow.next
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                break
            ##反转链表

        ###递归，记录

        return True
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        self.front_pointer = head       #记录开始节点

        def recursively_check(current_node = head):
            if current_node is not None:
                if not recursively_check(current_node.next):          #递归找到最后节点
                    return False
                if self.front_pointer.val != current_node.val:          ##回文判断
                    return False
                self.front_pointer = self.front_pointer.next            ##往下走
            return True

        return recursively_check()
