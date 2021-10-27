class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            nums[(nums[i]-1)%(n+1)] += (n+1);       //一位偏移，和n+1
        }
        int[] res = new int[2];
        for (int i = 0; i < n; i++) {
            if(nums[i]/(n+1)==2){
                res[0] = i+1;
            }else if(nums[i]/(n+1)==0){
                res[1] = i+1;
            }
        }
        return res;
    }
}