class Solution:                 ## 丑数1
    def isUgly(self, n: int) -> bool:
        while n:
            if n == 1:
                return True
            if n % 2 == 0:
                n /= 2              ##此时能够整除用/就可以，//表示有小数时只保留整数
            elif n % 3 == 0:
                 n /= 3
            elif n % 5 == 0:
                n /= 5
            else:
                return False
        return False
    def isUgly2(self, n: int) -> bool:
        # 原来： 判断次数3/2   一次除一个指数
        # 现在： 判断次数7/2   一次除了12/7个指数    效率提升了
        while n:
            if n == 1:
                return True
            if n % 30 == 0:             # 相当于做单词除法
                n /= 30
            elif n % 15 == 0:               # 相当于两次
                 n /= 15
            elif n % 10 == 0:
                n /= 10
            elif n % 6 == 0:
                n /= 6
            elif n % 5 == 0:
                n /= 5
            elif n % 3 == 0:
                n /= 3
            elif n % 2 == 0:
                n /= 2
            else:
                return False
        return False


# ####################################################丑数2
# 法1：堆操作：  （关键在于如何有序递增的找）   最小元素乘2、3、5，将其插入
# 使用堆 维护最小元素（需要构建堆和调整堆），每次将最小元素出堆，再计算*2，*3，*5的元素是否存在堆中，不在则将其插入
from heapq import heappop, heappush
class Ugly:
    def __init__(self):
        seen = {1, }
        self.nums = nums = []
        heap = []
        heappush(heap, 1)

        for _ in range(1690):                   #先进行1690次运算，将其预存储起来
            curr_ugly = heappop(heap)       #出堆
            nums.append(curr_ugly)
            for i in [2, 3, 5]:
                new_ugly = curr_ugly * i
                if new_ugly not in seen:        #看堆中是否已经存在
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)        #入堆
class Solution:
    u = Ugly()

    def nthUglyNumber(self, n):
        return self.u.nums[n - 1]


# 法2：动态调整   （三个指针其实能够遍历所有的最小元素，找到三个中最小的就是下一个丑数）
# 定义3个指针i2，i3，i5，它们都代表*2，*3，*5，开始时都指向数组nums的1，
# 这样一直计算min（nums[i2]*2,nums[i3]*3,nums[i5]*5）,那个最小相应的指针就往前一格1
# 相比使用堆，三个指针维护了最小的位置，不用一直调整堆
class Ugly:
    def __init__(self):
        self.nums = nums = [1, ]
        i2 = i3 = i5 = 0

        for i in range(1, 1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)

            if ugly == nums[i2] * 2:            # 移动已经更新的指针，
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1
class Solution:
    u = Ugly()
    def nthUglyNumber(self, n):
        return self.u.nums[n - 1]
