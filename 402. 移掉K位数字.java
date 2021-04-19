import java.util.Deque;
import java.util.LinkedList;

class Solution {
    public StringBuilder removeOne(StringBuilder sb, int k,int index){         //删掉一个数字
        if (k==0){
            return sb;
        }
        boolean b = false;
        for(int i=index; i<sb.length()-1; i++){
            if(sb.charAt(i)>sb.charAt(i+1)){            //前一个比后一个大
                b = true;
                sb.deleteCharAt(i);
                sb = removeOne(sb,k-1,i);                 //递归的往下删除
                break;
            }
        }
        if (!b) {
            sb.delete(sb.length() - k, sb.length());       //平序或升序
        }
        return sb;
    }
    public String removeKdigits(String num, int k) {
        //String：适用于少量的字符串操作的情况。
        //StringBuilder：适用于单线程下在字符缓冲区进行大量操作的情况。
        //StringBuffer：适用多线程下在字符缓冲区进行大量操作的情况。
        //String 从用的方法：连接concat()、提取substring()、charAt(i)、length()、equals()、indexOf()
        //StringBuffer支持以下几种操作函数：append（）、insert（）、replace（）、delete（）、reserve（）

        StringBuilder sb = new StringBuilder(num);
        sb = removeOne(sb,k,0);
        if (sb.length() > 0){
            while(sb.charAt(0) == '0'){
                sb.deleteCharAt(0);             //删除东西的时候不要用for循环
            }
        }
        if (sb.length()==0){
            return "0";
        }

        return sb.toString();
    }

        //贪心+单调栈（用来保持栈里边的元素的单调递增，当遇到减的时候就出栈顶）
    public String removeKdigits2(String num, int k) {
        Deque<Character> deque = new LinkedList<Character>();
        int length = num.length();
        for (int i = 0; i < length; ++i) {          //对前边比后边大的进行处理
            char digit = num.charAt(i);
            while (!deque.isEmpty() && k > 0 && deque.peekLast() > digit) {     //保持栈为单调递增
                deque.pollLast();                                       //一旦遇到变小，栈顶出栈
                k--;
            }
            deque.offerLast(digit);                 //进栈
        }

        for (int i = 0; i < k; ++i) {               //此时栈内为非递减，此时可以去除的还不够
            deque.pollLast();
        }

        StringBuilder ret = new StringBuilder();
        boolean leadingZero = true;
        while (!deque.isEmpty()) {
            char digit = deque.pollFirst();
            if (leadingZero && digit == '0') {
                continue;                   //将前边的多个0去掉
            }
            leadingZero = false;
            ret.append(digit);
        }
        return ret.length() == 0 ? "0" : ret.toString();
    }
}

