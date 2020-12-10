class Solution:
    def canJump(self, nums) :                     #超时-------------递归---按照要求依次往后计算
        i = 0
        leng = len(nums)
        def canJ(i):
            if i == leng-1:            #到达了结尾
                return True
            if i >= leng:
                return False
            for j in range(1,nums[i]+1):             #最大步数为nums[i]，我们要走0~nums[i]步
                if canJ(i+j) == True:
                    return True
            return False                      #到不了
        return canJ(0)

    #############我的想法2：能到最后的一定是   该元素下标+该元素数值 == len(nums)
    #### 可以试着迭代完数组看看有没有满足的，没有就直接返回False，有的话以这些节点为终点，递归的向前求，直到能找到开始节点




    ########方法3：贪心法（也不算吧）：：我们直接看  该元素下标+该元素数值 >= len(nums)  是否成立，
    # 成立就完事；否则从该元素向右的nums[i]中找，看是否有更远的，若有将其更新，否则继续走直到走不动为止

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:                    #直到右边的最远处
                rightmost = max(rightmost, i + nums[i])             #更新最右处
                if rightmost >= n - 1:
                    return True
        return False

nums = [3,2,1,0,4]
print(Solution().canJump(nums))

