class Solution1 {
    public int reverseBits(int n) {
        int rev = 0;
        for (int i = 0; i < 32 && n != 0; ++i) {
            rev |= (n & 1) << (31 - i);         //res和后边的相与
            n >>>= 1;
        }
        return rev;
    }
}

class Solution3{
    //第一次移动相邻的奇偶位（单位为1）
    //第二次将每两位当成一位
    //第三次将每4位
    //第四次 8
    //第五次 16    （也可以先16,8,4,2，1）
    private static final int M1 = 0x55555555; // 01010101010101010101010101010101
    private static final int M2 = 0x33333333; // 00110011001100110011001100110011
    private static final int M4 = 0x0f0f0f0f; // 00001111000011110000111100001111
    private static final int M8 = 0x00ff00ff; // 00000000111111110000000011111111

    public int reverseBits(int n) {
        n = n >>> 1 & M1 | (n & M1) << 1;       //n右移1位与M1与，n与M1与完左移1位，将结果再与
        n = n >>> 2 & M2 | (n & M2) << 2;
        n = n >>> 4 & M4 | (n & M4) << 4;
        n = n >>> 8 & M8 | (n & M8) << 8;
        return n >>> 16 | n << 16;
    }
}
