class Solution {
    public boolean isPerfectSquare(int num) {           //暴力
        if (num == 1){
            return true;
        }
        for (int i=1; i<=num/2; i++){
            if (i*i == num){
                return true;
            }
        }
        return false;
    }
    public boolean isPerfectSquare2(int num) {          //二分
        int begin = 1;
        int end = num;
        while (begin <= end){
            int mid =  begin + (end-begin)/2;
            if (mid*mid > num){
                end = mid-1;
            }else if(mid*mid < num){
                begin = mid+1;
            }else{
                return true;
            }
        }
        return false;
        }
    public boolean isPerfectSquare3(int num) {          //牛顿迭代:X(k+1) = X(k) - f(X(k))/f'(X(k))
        if (num < 2) return true;

        long x = num / 2;
        while (x * x > num) {           //因为这里的函数在[0,无穷]上为单调递增，初始取一半此时的x一定是大于等于平方根
            x = (x + num / x) / 2;
        }
        return (x * x == num);
    }

}
