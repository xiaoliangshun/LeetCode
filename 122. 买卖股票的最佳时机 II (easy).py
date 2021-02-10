class Solution:
    def maxProfit(self, prices):
        leng = len(prices)
        count = 0
        for i in range(leng-1):
            if prices[i] < prices[i+1]:                 ##从前往后找相邻的是升高的趋势的情况
                count += prices[i+1]-prices[i]
        return count



prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))