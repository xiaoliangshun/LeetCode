class Solution:
    def mySqrt(self, x):
        for i in range(1,x//2+2):       #这里是+2
            if i**2 > x:
                return i-1
            elif i**2 == x:
                return i
    def mySqrt2(self, x):           ##二分
        if x == 0:
            return 0
        start = 1
        end = x
        mid = 0
        while start <= end:
            mid = start + (end-start)//2
            print(start,end,mid)
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                end = mid-1
            else:
                start = mid+1
        if mid**2 < x:
            return mid
        else:
            return mid-1

        ##法3：
        #袖珍计算器算法
        # x ** 1/2 = (e ** lnx) ** 1/2 = e ** 1/2*lnx

        #法4：牛顿迭代法
        # 是一种可以用来快速求解函数零点的方法
        #f(x) = x**2 - C   的零点问题

print(Solution().mySqrt2(0))
