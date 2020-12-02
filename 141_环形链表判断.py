# # Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head):
        set1 = set()
        while head.next != None:                    #放元素也是可以的，这里在元素里边检查用的in也是检查地址
            if id(head) in set1:                   #id(value1)  # 获取value的地址---->>>ctypes.cast(地址, ctypes.py_object).value 获取地址的值
                return True                         #同样的我们也可以在第一次经过节点的时候将他的值置为空，就相当于标记，每次都检查是否为空
            else:
                set1.add(id(head))
                print(set1)
            head = head.next
        return False


    def hasCycle1(self,head):           #快慢指针，就跟龟兔赛跑一样，只要有循环那么兔子一定能再次赶上乌龟（还是要基于地址）
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:     #slow节点，fast节点
            if not fast or not fast.next:          #没有环的话，两步走，要检查当前和下一步是否存在
                return False
            slow = slow.next              #一步走
            fast = fast.next.next          #两步走 (两个指针之间的速度差距要是1，不然可能会错过)（每次他们之间的差距都会拉开1，这样的话如果有环的话，他们之间的反向距离就近了1）
        return True
    #法3：可以将节点一个一个的删除（将其next指向自己），如果没有环，那莫删到最后的next一定是空；；如果有环，那莫最后的next是指向自己的
    #就是看有没有出口，如果有出口就一定有一个next指向空。关键就是缩小范围（每次都将链断开，避免了循环）



root = ListNode(3)
root1 = ListNode(2)
root2 = ListNode(0)
root3 = ListNode(-4)
root.next = root1
root1.next = root2
root2.next = root3
root3.next = root1

print(Solution().hasCycle1(root))

