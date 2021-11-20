package com.xls;

/**
 * @author XLS
 * @version 1.0
 */
public class leet {
    //方法1 先将数组按照绝对值进行排序，直接平方即可
    //充分利用原有数组有序的特点
    //改进：其实两边大的开始归并，就不用查找分解的位置了
    public static void main(String[] args) {
        new leet().sortedSquares(new int[]{-4,-1,0,3,10});
    }

    //方法1
    public int[] sortedSquares(int[] nums) {
        //1. 找到第一个正数，讲数组分成左右两个部分进行归并排序
        int index = getIndex(nums);
        //2. 分成两部分进行归并
        return mergeSort(nums, index);
    }

    public int getIndex(int[] nums){
        int start = 0, end = nums.length-1;
        while(start<end){
            int mid = start + (end-start)/2;
            if(nums[mid]>=0){
                end = mid;
            }else{
                start = mid+1;
            }
        }
        return start;
    }

    //按照绝对值进行排序[0,index-1] 和 [index,...]
    public int[] mergeSort(int[] nums, int index){
        int left = index-1;
        int right = index;
        int[] res = new int[nums.length];
        int i = 0;
        while(left>=0 && right<nums.length){
            if(Math.abs(nums[left])>Math.abs(nums[right])){
                res[i++] = nums[right] * nums[right];
                right++;
            }else{
                res[i++] = nums[left] * nums[left];
                left--;
            }
        }

        while(left>=0){
            res[i++] = nums[left] * nums[left--];
        }
        while(right<nums.length){
            res[i++] = nums[right] * nums[right++];
        }
        return res;
    }
}
