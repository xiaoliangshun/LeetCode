class Solution {
    public int findComplement(int num) {
        String b = Integer.toBinaryString(num);         //转为二进制
        int leng = b.length();
        return (int) (Math.pow(2,leng)-1 -num);         //正数补码为2的n次方减1
    }
}

class Solution1 {
    public int findComplement(int num) {
        int ans=0,i=0;
        while(num!=0) {
            ans+=(~(num & 1))*Math.pow(2,i++);          //位运算取反
            num>>=1;            //移位操作
        }
        return ans;
    }
}
//    位逻辑运算符包含 4 个：&（与）、|（或）、~（非）和 ^（异或）

//还可以使用异或的性质：   a^b=c 那么 a^c=b 反向求解