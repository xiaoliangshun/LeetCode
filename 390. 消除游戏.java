class Solution {
    //最原始的方法实现：
    // 创建一个对应的数组依次将为true的元素设为false直到只剩一个true
    public int lastRemaining(int n) {
        boolean[] a = new boolean[n+1];
        a[0] = false;
        for (int i=1; i<n+1; i++){
            a[i] = true;
        }
        int i=1;
        boolean reverse = false;        //控制从前往后，还是从后往前
        int count = n;                  //记录true的个数
        int begin = 1;              //边界 [begin,end]
        int end = n;                //边界
        while(count > 1){
            if (!reverse){
                boolean now = false;             //表示当前是否已经改过
                while(i <= end && count > 1){
                    if (a[i] == true && !now){
                        a[i] = false;
                        count--;
                        now = true;
                    }else if(a[i] == true && now){
                        now = false;
                    }
                    i++;
                }
                reverse = true;
                begin += 1;
                if (a[end] == false) {
                    end -= 1;
                }
                i = end;
            }else{
                boolean now = false;            //表示当前是否已经改过
                while(i >= begin && count > 1){
                    if (a[i] == true && !now){
                        a[i] = false;
                        count--;
                        now = true;
                    }else if(a[i] == true && now){
                        now = false;
                    }
                    i--;
                }
                reverse = false;
                end -= 1;
                if (a[begin] == false){
                    begin += 1;
                }
                i = begin;
            }
        }
        for (int j=1; j<n+1; j++){
            if (a[j] == true){
                return j;
            }
        }
        return 0;
    }

    public static void main(String args[]){
        Solution s = new Solution();
        System.out.println(s.lastRemaining(5));
    }

    //法2：数学的递归方法
    //关键在于找到递归式
    //https://leetcode-cn.com/problems/elimination-game/solution/mei-ri-suan-fa-day-85-tu-jie-suan-fa-yi-xing-dai-m/
    public int lastRemaining2(int n){
        if (n==1){
            return 1;
        }else {
            return 2*(n/2+1-lastRemaining2(n/2));
        }
    }
}