class Solution {
    public List<Boolean> prefixesDivBy5(int[] nums) {
        int temp = 0;
        List<Boolean> li = new ArrayList<>();
        for(int i=0; i<nums.length; i++){
            temp = (2*temp + nums[i])%5;    //除5的原因是因为（若果是5的倍数在下一轮要先*2再+num[i]，*2的部分也一定是5的倍数）
            li.add(temp == 0);
        }
        return li;
    }
}