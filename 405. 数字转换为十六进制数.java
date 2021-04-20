class Solution{
    public String toHex(int num) {
        //计算机上本就是补码存储的，是负数的话也只用按照整数一样的处理方法
        if (num == 0) { return "0"; }   // 0特殊处理
        char[] hex = "0123456789abcdef".toCharArray();   // 相当于映射关系
        StringBuilder ans = new StringBuilder();
        while (num != 0) {
            int temp = num & 0xf;   // 取低4位的十进制值!!!
            ans.append(hex[temp]);  // 映射对应字符
            num >>>= 4;             // 逻辑右移4位
        }
//         while的循环条件保证了不会出现前导0
//         但是从低位开始转换多了一步reverse反转
        return ans.reverse().toString();
    }
}
