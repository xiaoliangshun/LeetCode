class Solution:
    def trap(self, height) :
        s = 0
        i = 0 ; j = len(height)-1        #开始和结束
        lmax = 0; rmax = 0       #记录左右点
        min1 = 0             #上此左右的最小值
        while i < j:
            while i<len(height) and height[i] <= lmax: i += 1         #从左向右找第一个大于上一次高点的位置
            while j>=0 and height[j] <= rmax: j -= 1         #从右向左找第一个大于。。。
            if i == len(height) or j == -1:
                return s
            num = min(height[i],height[j])                #当前的较低点
            for index in range(i+1,j):                #i~j中间的点
                if height[index] < num:
                    if height[index] <= min1:             #还小于上此的最小值
                        s += num - min1           #免得重复计算（这才是没有计算的部分）
                    else:
                        s += num - height[index]                    #所加值应为差值部分
            min1 = num                   #更新上此最小点
            lmax = rmax = num            #这样的话是较小值的点找更大的点，较大的点则不用找
        return s

   # https://leetcode-cn.com/problems/trapping-rain-water/solution/jie-yu-shui-by-leetcode/
    ######方法2：   从左到右遍历一边数组，算出每个每个元素左边的最大值； 再从右到左遍历一遍数组计算除每个元素右边的最大值；（思路很好）
    #########        最后就是对比每一个元素左右的最大值中的较小者与自己的差距，计算蓄水量

    ######方法3：  单调栈：栈中存储元素为递减，若当前元素高于栈顶元素，栈顶的元素必定有积水，出栈，计算与当前元素的积水量，该元素再与次栈顶元素进行对比
    #######           继续计算，直到栈里头没有元素了或当前元素走到最后

    ######方法4： 双指针：若左指针较大，则右边说了算，若当前小于右边的相对最大值，有积水，若大于则更新最大值；
    #######             若右指针较大，左边说了算，。。。。

nums = [5,5,1,7,1,1,5,2,7,6]
print(Solution().trap(nums))