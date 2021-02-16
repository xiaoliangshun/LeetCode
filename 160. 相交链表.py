class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

##找到两个链表相交部分的开始节点
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:        #双指针法：本质是找两个链表结尾相同的部分
        hA = headA                                                                   #这种比较方法就是消除了两个链表前边不相同的长度部分（两个链表长度差）
        hB = headB                                                                               #消除长度差： 拼接两链表
        count = 0
        while hA.next or hB.next:     #只要有一个没走到结尾
            if hA.val == hB.val and count == 2:
                return hA
            if hA.next:
                hA = hA.next
            else:
                count += 1
                hA = headB         ##从两一个链表头开始
                                                                        ###？？？？？？题目有问题
            if hB.next:
                hB = hB.next
            else:
                count += 1
                hB = headA

    class Solution(object):
        def getIntersectionNode(self, headA, headB):            #双指针法：写法更简便的
            ha, hb = headA, headB
            while ha != hb:
                ha = ha.next if ha else headB
                hb = hb.next if hb else headA
            return ha
