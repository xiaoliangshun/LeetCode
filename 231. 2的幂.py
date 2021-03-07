class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        while n > 2:
            if n % 2 == 1:
                return False
            n = n // 2
        if n == 2:
            return True

        ##方法一：位运算：获取二进制中最右边的 1      n & (-n)
    def isPowerOfTwo2(self, n):
        if n == 0:
            return False
        return n & (-n) == n        #(-x的补码表示为取反再加1，与x与的结果能得到x最右边的一位为1，其余为0)若是2的幂，则这个1只能做高位
        #方法三：位运算：去除二进制中最右边的 1           n & (n-1)
    def isPowerOfTwo3(self, n):
        if n == 0:
            return False
        return n & (n-1) == 0

print(Solution().isPowerOfTwo(16))