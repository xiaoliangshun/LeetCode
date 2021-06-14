class Solution {
	//顺序排序结果最大
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);      //排序
        int sum =0;
        for(int i=0; i<nums.length; i+=2){
            sum += nums[i];
        }
        return sum;
    }
}