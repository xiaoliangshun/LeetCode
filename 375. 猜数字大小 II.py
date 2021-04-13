class Solution:
    # 本题的意思是求能够猜到[所有数]的，而且是[最少]钱
    # 关键是选什么什么进行比较
    # cost(1,n)=i+max(cost(1,i−1),cost(i+1,n))

    # 法1：递归求解
    import sys
    def getMoneyAmount(self, n: int) -> int:
        def getMoney(low,hight):
            if low >= hight:
                return 0
            cost = sys.maxsize
            for i in range((low+hight)//2,hight+1):                 # 优化后，只计算后边（因为后边的更大）
                rest = i + max(getMoney(low,i-1),getMoney(i+1,hight))
                cost = min(cost,rest)
            return cost

        return getMoney(1,n)

    # 法2：动态规划
    # 充分利用之前计算的结果，从头开始
#https://leetcode-cn.com/problems/guess-number-higher-or-lower-ii/solution/cai-shu-zi-da-xiao-ii-by-leetcode/