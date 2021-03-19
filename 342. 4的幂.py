class Solution:
    def isPowerOfFour(self, n: int) -> bool:            ##暴力法
        if n <= 0:
            return False
        while n > 1:
            if n % 4 != 0:
                return False
            n = n // 4
        return True
print(Solution().isPowerOfFour(16))

##使用数组预存，虽然看起来一点技巧也没有，但是能够充分利用题中的条件，找到最适合的方法
class Powers:
    def __init__(self):
        max_power = 15
        self.nums = nums = [1] * (max_power + 1)
        for i in range(1, max_power + 1):
            nums[i] = 4 * nums[i - 1]

class Solution:
    p = Powers()
    def isPowerOfFour(self, num: int) -> bool:
        return num in self.p.nums

#如果数字为4 的幂 x = 4^a,则 a = log4 x = 1/2 log2 x 是否为整数即可
from math import log2
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and log2(num) % 2 == 0

#位操作
# 我们首先检查 num 是否为 2 的幂：x > 0 and x & (x - 1) == 0  保证只有一个1
# 4 的幂与数字 (101010...10）相与的结果为0  （4的幂再低奇数位上只有一个1）
# (101010...10）用16进制表示为：(aaaaaaaa)16
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num & 0xaaaaaaaa == 0

##与上一中方法不一样的就是num可以用3取余
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num % 3 == 1


