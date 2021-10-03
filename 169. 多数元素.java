class Solution {
    public int majorityElement(int[] nums) {
        //将所有不相等的元素对去掉，剩下的就是。
        //众数出现的次数比非众数多（能抵消掉）
        int count = 0;
        int candidate = null;
        for(int i=0; i<nums.length; i++){
            if(count==0) candidate = nums[i];       //更改候选
            count += (candidate==nums[i])?1:-1; 
        }
        return candidate;
    }
}

