#法1 ： 一直除3，直到为1    O(log 3 n)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n >= 1:
            if n == 1:
                return True
            if n % 3 != 0:
                return False
            n /= 3
#法2 ： 将10进制的n换成3进制的数组，看是否只含有一个1      O(log 3 n)
# 有点多此一举，因为在转换乘3进制的时候就是除3的过程


#法3 ： 数学法：   3**i = n ，那莫i = log 3 n  = log b n / log b 3


#法4 ： 我们只用计算  1162261467 % n == 0    （1162261467为最大的3的幂）
# 最大的3的幂为 3 ** max     if n == 3**i ,则能整除  （因为3是质数，所有不能分解了，他只有3**x的质数）
    def isPowerOfThree4(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0