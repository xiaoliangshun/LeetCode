class Solution {
    //还可以使用数组
    //或遍历两遍
    public ListNode middleNode(ListNode head) {
        ListNode fast = head;   //快指针
        ListNode slow = head;   //慢指针
        while(fast.next != null){
            if(fast.next.next != null){
                fast = fast.next.next;
                slow = slow.next;
            }else{
                return slow.next;		//偶数情况下
            }
        }
        return slow;	//奇数情况下
    }
}