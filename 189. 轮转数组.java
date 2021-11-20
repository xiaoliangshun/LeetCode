class Solution {
    //方法1 直接返回一个新的数组

    public void rotate(int[] nums, int k) {
        k %= nums.length;
        if(k % nums.length == 0) return;
        //多少个圈子
        int n = gcd(nums.length,k);         //圈数为长度和k的最大公约数
        for(int i=0; i<n; i++){
            ro(nums,k,i);
        }

    }

    //只将从begin开始，每隔k个，的圈进行移动
    public void ro(int[] nums , int k, int begin){
        int temp = nums[begin];     //保留第一个元素
        int now = begin;
        int nextIndex = (now-k+nums.length) % nums.length;   //循环[前一个放入该点的位置]
        while(nextIndex != begin){
            nums[now] = nums[nextIndex];      //将前一个点放入该点
            now = nextIndex;
            nextIndex = (now-k+nums.length) % nums.length;
        }
        nums[now] = temp;       //添回去
    }

    public int gcd(int x, int y) {          //辗转相除法求最大公约数
        return y > 0 ? gcd(y, x % y) : x;
    }
}

//法2 直接使用额外数组
//法3 现将数组完全反转， 再将前k个 和 后边的反转【第一次反转实现了前k个和后边的部分颠倒，第二次分组反转使得其组内的先后顺序不变】
//该方法适合于将数组中的值进行循环移动
class Solution1 {
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }

    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start += 1;
            end -= 1;
        }
    }
}