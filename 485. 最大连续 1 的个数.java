class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxLeng = 0,currentLeng = 1;
        if (nums[0]==0) currentLeng = 0;
        for (int i=0; i<nums.length-1; i++){
            if(nums[i] == 1 && nums[i+1] == 1){         //i+1是工作位置
                currentLeng++;
            }else if(nums[i] == 1 && nums[i+1] == 0){           //更新
                if (currentLeng>maxLeng) maxLeng = currentLeng;
                currentLeng = 0;
            }else if(nums[i] == 0 && nums[i+1] == 1){           //重新开始
                currentLeng = 1;
            }
        }
        if (currentLeng>maxLeng) maxLeng=currentLeng;
        return maxLeng;
    }
}
class Solution1 {
    //完全可以遇到0再进行最大值计算
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxCount = 0, count = 0;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) {
                count++;
            } else {
                maxCount = Math.max(maxCount, count);
                count = 0;
            }
        }
        maxCount = Math.max(maxCount, count);
        return maxCount;
    }
}
