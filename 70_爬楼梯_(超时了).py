class Solution:
    def climbStairs(self, n):
        def flower(n,count):
            if n == 0:                  #出口
                return 1
            elif n < 0:
                return 0

            return flower(n-1,count)+flower(n-2,count)           #左右的和（可以通过话递归树，找到当前状态到下一个状态的关系）

        return flower(n,0)

print(Solution().climbStairs(30))
