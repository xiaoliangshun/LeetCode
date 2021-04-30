class Solution {
    //遍历+二分
    public double sum_preN(long base,long n){             // 使用等比数列求和公式
        return (1-Math.pow(base,n)) / (1-base);
    }

    public String smallestGoodBase(String n) {
        long nn = Long.valueOf(n);        //String转int； Integer.valueOf(s)           String s1 = String.valueOf(n) int转String
        for (int i=Long.toBinaryString(nn).length(); i>1; i--){      //长度由长到短(进制由小到大)
            long l = 2,r = nn-1;
            while (l<=r){           //二分
                long mid = l + (r-l)/2;
                double v = sum_preN(mid,i);
                if(v>nn){
                    r = mid-1;
                }else if(v<nn){
                    l = mid+1;
                }else{
                    return String.valueOf(mid);     //返回进制
                }
            }
        }
        return "s";
    }
    public static void main(String[] args){
        Solution s = new Solution();
        System.out.println(s.smallestGoodBase("1000000000000000000"));
        System.out.println(s.sum_preN(999999999,9999));
    }
}

//class Solution:
//        def smallestGoodBase(self, n: str) -> str:
//        n = int(n)
//        # 上面提到的 base 进制转十进制公式。
//        # 使用等比数列求和公式可简化时间复杂度
//        def sum_with(base, N):
//        return (1 - base ** N) // (1 - base)
//        # return sum(1 * base ** i for i in range(N))
//        # bin(n) 会计算出 n 的二进制表示， 其会返回形如 '0b10111' 的字符串，因此需要减去 2。
//        for N in range(len(bin(n)) - 2, 0, -1):
//          l = 2
//          r = n - 1
//        while l <= r:
//          mid = (l + r) // 2
//        v = sum_with(mid, N)
//
//        if v < n:
//          l = mid + 1
//        elif v > n:
//          r = mid - 1
//        else:
//          return str(mid)


