class Solution {
    public int[] countBits(int n) {
        int[] a = new int[n+1];
        a[0] = 0;
        int last = 0;       //表示下一次的最大次幂
        for(int i=1; i<=n; i++){
            if(i == Math.pow(2,last)){
                a[i] = 1;
                last++;
            }else{
                a[i] = 1 + a[i-(int)Math.pow(2,last-1)];       //将其分解为2的last次方+剩余的项（动态规划）
            }
        }
        return a;
    }
}
class Solution {
    public int[] countBits(int n) {
        int[] bits = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            bits[i] = bits[i & (i - 1)] + 1;            //i&(i-1)表示将最后一位的1变成0，【太棒了】
        }
        return bits;
    }
}