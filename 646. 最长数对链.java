class Solution {		//超时
    public int findLongestChain(int[][] pairs) {
        if(pairs.length == 0) return 0;
        sort1(pairs);
        return find(0,Integer.MIN_VALUE,pairs);
    }
    public int find(int index, int lastMax, int[][] pairs){
        if(index > pairs.length-1) return 0;
        if(lastMax < pairs[index][0]){      //可以加入[选择和不选择->穷举]
            int f1 = find(index+1, pairs[index][1], pairs)+1;     //选择当前元素
            int f2 = find(index+1, lastMax, pairs);        //不选择当前元素
            return f1>f2 ? f1 : f2;
        }else{
            return find(index+1,lastMax,pairs);
        }
    }
    public static void sort1(int[][] arr){
        for(int i=0; i<arr.length-1; i++){
            for (int j = 0; j <arr.length-1-i ; j++) {
                if(arr[j][0] > arr[j+1][0]){
                    int[] temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
}

class Solution1 {		//动态规划
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, (a, b) -> a[0] - b[0]);
        int N = pairs.length;
        int[] dp = new int[N];
        Arrays.fill(dp, 1);

        for (int j = 1; j < N; ++j) {
            for (int i = 0; i < j; ++i) {
                if (pairs[i][1] < pairs[j][0])
                    dp[j] = Math.max(dp[j], dp[i] + 1);		//dp[j]表示在j前边的长数
            }
        }

        int ans = 0;
        for (int x: dp) if (x > ans) ans = x;
        return ans;
    }
}
class Solution {		//贪心【按照pairs的后便元素排序】->每次都是找占用最少的，也就是后边元素最小的值
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, (a, b) -> a[1] - b[1]);
        int cur = Integer.MIN_VALUE, ans = 0;
        for (int[] pair: pairs) if (cur < pair[0]) {
            cur = pair[1];
            ans++;
        }
        return ans;
    }
}

