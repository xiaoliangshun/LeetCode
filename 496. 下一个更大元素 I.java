import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] a = new int[nums1.length];
        for (int i=0; i<nums1.length; i++){
            a[i] = -1;
        }
        int k = 0;
        while (k < nums1.length) {
            int s = 0;
            while(nums2[s] != nums1[k]) s++;
            for (int i = s+1; i < nums2.length; i++) {
                if (nums2[i] > nums1[k]) {            //寻找右边大于已经标记的num1中的数
                    a[k] = nums2[i];
                    break;
                }
            }
            k++;
        }
        return a;
    }


    public class Solution1 {
            //单调栈：（可以在O(n)的时间复杂度内找出所有元素的右边较大值）：
            //单调栈的用处就是找到数组中左边或右边比每个元素大或小的数
            //保持栈为单调递减，
            //1.比栈顶小就入栈，   2.比栈顶大就出栈，记录当前元素
            //思路：先用单调栈计算nums2中素偶偶有元素右边比他大的值，将下标放入hash中，nums1遍历即可
        public int[] nextGreaterElement(int[] nums1, int[] nums2) {
            int len1 = nums1.length;
            int len2 = nums2.length;

            Deque<Integer> stack = new ArrayDeque<>();
            Map<Integer, Integer> map = new HashMap<>();
            // 先处理 nums2，把对应关系存入哈希表
            for (int i = 0; i < len2; i++) {
                while (!stack.isEmpty() && stack.peekLast() < nums2[i]) {
                    map.put(stack.removeLast(), nums2[i]);
                }
                stack.addLast(nums2[i]);
            }

            // 遍历 nums1 得到结果集
            int[] res = new int[len1];
            for (int i = 0; i < len1; i++) {
                res[i] = map.getOrDefault(nums1[i], -1);
            }
            return res;
        }
    }

}
