class Solution {
    public List<Integer> findDuplicates(int[] nums) {
		//因为最大数是n，所以每当有一个数过来就在原数组的基础上的对应计数位置加上n（这样的话如果记录了两次，那么结果一定大于2*n）
        int n = nums.length;
        List<Integer> ans = new ArrayList<>();

        for(int i:nums){
            nums[(i-1)%n]=nums[(i-1)%n]+n;		//关键问题在于：数的范围在1-n，而下标的范围在0~n-1，这就要求我们平移了（将对数值为X的计数放在x-1的位置上）
        }
        for(int i=0;i<n;i++){
            if(nums[i]>2*n){
                ans.add(i+1);
            }
        }
        return ans;
    }
}
