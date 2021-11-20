class Solution {
    public int maxSubArray(int[] nums) {
        //动态规划
        //将问题拆分为计算每一个位置左侧的能连起来的最大值，计算到最后就可以了
        //计算的每一个左边的最大值都能用到右边
        if(nums.length==1) return nums[0];
        int max = nums[0];  //全局最大值
        int leftMax = nums[0];       //记录左侧最大值
        for(int i=1; i<nums.length; i++){
            if(leftMax>0){
                leftMax += nums[i];     //要左边的
            }else{
                leftMax = nums[i];      //不要左边的
            }
            max = leftMax > max ? leftMax : max ;
        }
        return max;
    }
}

//还可以使用分治进行求解