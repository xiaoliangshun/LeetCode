class Solution:                     #123. 买卖股票的最佳时机 III head       超时！！！！！！！
    def maxProfit(self, prices):
        def maxP(begin,end):         #记录只选择一次时的最大收益
            count = 0
            for i in range(begin,end+1):
                for j in range(i,end+1):
                    count = max(count,prices[j]-prices[i])      #找出中间跨度最大的数字O（N**2）
            return count

        leng = len(prices)
        Max = 0
        for i in range(leng):
            Max = max(Max,maxP(0,i)+maxP(i,leng-1))           #按照每个分割点分别对两边就Max利益
        return Max

            ##看不懂
        ##https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/di-gui-dong-tai-gui-hua-tan-xin-er-fen-4-xxd5/

prices = [14,9,10,12,4,8,1,16]
print(Solution().maxProfit(prices))