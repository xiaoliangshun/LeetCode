import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

class Solution1 {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] ret = new int[n];
        Arrays.fill(ret, -1);                       //将ret数组全部填充为1
        Deque<Integer> stack = new LinkedList<Integer>();
        for (int i = 0; i < n * 2 - 1; i++) {               //当2n-1个元素都放进去的时候才算循环结束
            while (!stack.isEmpty() && nums[stack.peek()] < nums[i % n]) {              //用%很好的处理了循环的问题
                ret[stack.pop()] = nums[i % n];
            }
            stack.push(i % n);          //栈内存放的是没有找到的右边大数值的下标（这样就不用指针来记录了）
        }
        return ret;
    }
}
//三个关键：
//        选用单调栈提速。
//          「 对于找最近一个比当前值大/小」的问题，都可以使用单调栈来解决。⌟
//          栈可以很好的保存原始位置，最近影射栈顶。题目要求更大，因此更大即解--出栈，更小则入栈
//          「 栈内存放的永远是还没更新答案的下标。⌟
//        二倍数组长度，简化遍历。
//          要找的目标，要么在当前元素之前，要么在之后，因此两次遍历一定能覆盖到。即方便遍历又有了退出条件。
//          如果游标无限 +1取模，也是要另设置退出条件的
//        初值赋-1，解决最大值老无所依。