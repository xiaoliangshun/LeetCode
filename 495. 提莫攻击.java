class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        int sub = 0;        //计算重叠的时间
        for (int i=0; i<timeSeries.length-1; i++){
            if(timeSeries[i]+duration > timeSeries[i+1]) sub += timeSeries[i]+duration-timeSeries[i+1];
        }
        return duration*timeSeries.length-sub;      //减掉重叠的时间
    }
}
class Solution1 {
    //累加，
    // 在timeSeries[i+1]当前位置截断，不影响后边的(分割)
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        int n = timeSeries.length;
        if (n == 0) return 0;

        int total = 0;
        for(int i = 0; i < n - 1; ++i)
            total += Math.min(timeSeries[i + 1] - timeSeries[i], duration);
        return total + duration;
    }
}