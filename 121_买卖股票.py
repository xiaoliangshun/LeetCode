class Solution:
    def maxProfit(self, prices) :                 #找最小点，并计算当前卖出利益的最大收益
        max_money = 0
        min_cost = 1e9             #1*10^9  很大
        for p in prices:
            max_money = max(max_money,p-min_cost)               #往大了找 (两个值都更新)
            min_cost = min(min_cost,p)                   #往小了去
        return max_money
    ###########   时间复杂度:O(n)


prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))