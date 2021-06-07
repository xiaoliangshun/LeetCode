class Solution {
    public boolean canBeEqual(int[] target, int[] arr) {
        int[] a = new int[1001];          //计数
        for(int i=0; i<target.length; i++){
            a[target[i]]++;    //看两个数组能否抵消（也可以放在set集合，对比一下）
            a[arr[i]]--;
        }
        for(int i=0; i<1001; i++){
            if(a[i] != 0) return false;
        }
        return true;
    }
}