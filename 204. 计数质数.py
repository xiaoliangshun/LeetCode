class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        list1 = [False] * n         #
        x = 2
        while x < n:
            for i in range(2,(n-1)//x +1):         #将x的所有倍数(从2开始)全设为True
                list1[i*x] = True
            x += 1
        return list1.count(False)-2       #减去0和1两个False

print(Solution().countPrimes(2))