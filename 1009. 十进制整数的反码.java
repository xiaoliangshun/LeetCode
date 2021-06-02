class Solution {
    public int bitwiseComplement(int n) {
        if(n==0){ return 1;}
        int temp = 0;
        while(Math.pow(2,temp)<=n) temp++;      //找到大于n的二进制的长度
        return (int)Math.pow(2,temp)-1-n;       //原码与补码的和全1
    }
}