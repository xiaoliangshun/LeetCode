class Solution:
    # #法1 ：动态规划法，，
    # n首先一定是分成两个数的，然后如果连个数还能再分就继续。
    # 先初始化 [0,1,2,3] 然后后边的就是计算 dp[i-j]*dp[j] 中的最大值（因为我们从前向后构造dp，此时的dp[x]已经是最大的值了）
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            max1 = 0
            for j in range(1, i // 2 + 1):
                max1 = max(max1, i, dp[j] * dp[i - j])
            dp[i] = max1
        return dp[n]

    # 动态规划优化
    # 分解过程中我们发现，使用大于3的数一定能分解乘2**x * 3**y 的积（且这个时候积最大）
    def integerBreak2(self, n: int) -> int:
        if n <= 3:
            return n-1
        dp = [0] * (max(5,n+1))
        dp[1], dp[2], dp[3], dp[4] = 1, 2, 3, 4
        for i in range(5, n + 1):            #从第5个开始
            dp[i] = max(2*dp[i-2], 3*dp[i-3])
        return dp[n]


    #数学法：证明出来的（不懂）
    def integerBreak3(self, n: int) -> int:
        if n <= 3:
            return n - 1

        quotient, remainder = n // 3, n % 3
        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return 3 ** (quotient - 1) * 4
        else:
            return 3 ** quotient * 2

    #我的数学法： 能把所有大于1的数分解乘若干2和3的和，他们的乘积就是结果
    # 还有一种方法就是将n分解为两个最相近的数（偶数则是两个相同的数，奇数则相差1），继续分解到2和3为止
    def integerBreak4(self, n: int) -> int:
        if n <= 3:
            return n - 1
        count3 = 0
        count2 = 0
        while n >= 3:
            n -= 3
            count3 += 1
        while n >= 2:
            n -= 2
            count2 += 1

        if n == 0:
            return 3 ** count3 * 2 ** count2
        elif n == 1:
            return 3 ** (count3 - 1) * 2 ** (count2 + 2)