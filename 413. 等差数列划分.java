class Solution {
    //公式法：my，，有点问题？？？？？？？？？
    public int numberOfEquSub(int leng){
        if (leng==3){
            return 1;
        }else{
            return (leng-1)*(leng-2)/2;
        }
    }

    public int numberOfArithmeticSlices(int[] nums) {
        int sub = 0;                //两者的差
        boolean b = false;             //代表是否是新的开始
        int leng = 1;                   //表示等差的长度
        int sum = 0;                    //记录等差数组的个数
        for (int i=1; i<nums.length; i++){              //i表示当前元素
            if (!b){            //重新开始
                sub = nums[i]-nums[i-1];
                b = true;
                leng ++;
            } else{
                if (sub == nums[i]-nums[i-1]){
                    leng++;
                }else{
                    if (leng > 2){
                        sum += numberOfEquSub(leng);
                    }
                    leng = 1;           //初始化
                    b = false;
                }
            }
        }
        return sum;
    }
}

class Solution1 {
    //动态规划
    //dp[i]表示除了dp[i-1]组成的等差数列，还能组成的等差数列个数
    // (去掉能组成等差的最前边的元素就一样能组成像dp[i-1]一样个数的等差数列，还有一个是从组成等差的最前边到i)
    public int numberOfArithmeticSlices(int[] A) {
        int[] dp = new int[A.length];
        int sum = 0;
        for (int i = 2; i < dp.length; i++) {
            if (A[i] - A[i - 1] == A[i - 1] - A[i - 2]) {
                dp[i] = 1 + dp[i - 1];
                sum += dp[i];
            }
        }
        return sum;
    }
}
class Solution2 {
    //优化的动态规划
    public int numberOfArithmeticSlices(int[] A) {
        int dp = 0;
        int sum = 0;
        for (int i = 2; i < A.length; i++) {
            if (A[i] - A[i - 1] == A[i - 1] - A[i - 2]) {
                dp = 1 + dp;
                sum += dp;
            } else
                dp = 0;
        }
        return sum;
    }
}
class Solution3 {
    //公式法
    public int numberOfArithmeticSlices(int[] A) {
        int count = 0;
        int sum = 0;
        for (int i = 2; i < A.length; i++) {
            if (A[i] - A[i - 1] == A[i - 1] - A[i - 2]) {
                count++;
            } else {
                sum += (count + 1) * (count) / 2;
                count = 0;
            }
        }
        return sum += count * (count + 1) / 2;
    }
}
