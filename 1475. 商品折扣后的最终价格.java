import java.util.Stack;

class Solution {
    //使用单调栈来处理：维持栈内的元素递增
    public int[] finalPrices(int[] prices) {
        Stack<Integer> s=new Stack<>();
        for(int i=0;i<prices.length;i++){
            //能在栈里面呆着说明还没找到右边第一个比它小的
            while(!s.isEmpty()&&prices[s.peek()]>=prices[i]){           //栈非空而且栈顶元素大于等于添加的元素
                prices[s.pop()]-=prices[i];
            }
            s.push(i);  //进栈(存的是元素的下标)
        }
        return prices;
    }
}