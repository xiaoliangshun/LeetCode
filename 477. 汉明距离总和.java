class Solution {
    // 超时
    public int HamDis(int a, int b){
        int dis = 0;
        while (a>0 || b>0){
            if (a>0 && b>0){           //都还在
                if (a%2 != b%2) {           //相同位置的数不相等
                    dis++;
                }
                a /= 2;
                b /= 2;
            }else{              //其中一个结束了
                if (a>b){
                    if( a % 2 == 1){
                        dis++;
                        a /= 2;
                    }
                }else {
                    if(b % 2 == 1){
                        dis++;
                        b /= 2;
                    }
                }
            }
        }
        return dis;
    }
    public int totalHammingDistance(int[] nums) {
        int sum = 0;
        for(int i=0; i<nums.length; i++){
            for(int j=i+1; j<nums.length; j++) {
                sum += HamDis(nums[i],nums[j]);
            }
        }
        return sum;
    }
}

class Solution1 {
        public int totalHammingDistance(int[] nums) {
            int sum = 0;
            for(int i=0; i<nums.length; i++){
                for(int j=i+1; i<nums.length; j++) {
                    int a = nums[i]^nums[j];            //异或操作，然后累计1的个数
                    System.out.println(a);
                    while (a > 0){
                        if(a%2 == 1){
                            sum++;
                            a /= 2;
                            System.out.println(a);
                        }
                    }
                }
            }
            return sum;
        }
    }

class Solution2 {
    //每一个数其实都可以单独处理,我们假设第k位有两个0和两个1，
    // 那么随意选择两个数，如果都是0或都是1忽略，那么累计的汉明距离一定为不同组内元素个数的积2*2
    public int totalHammingDistance(int[] nums) {
        if (nums.length==0){
            return 0;
        }
        int[] a = new int[32];          //存放该位置为1的个数
        for (int num : nums){
            int i = 0;
            while (num > 0){
                if(num%2==0){
                    a[i]++;             //第i位
                    num /=2;
                    i++;
                }
            }
        }
        int sum = 0,n=nums.length;
        for (int k :a){
            sum += k*(n-k);                 //1的个数乘以0的个数
        }
        return sum;
    }
}