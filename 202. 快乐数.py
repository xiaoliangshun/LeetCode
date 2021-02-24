class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0
        times = 100
        while times:
            while n:
                count += (n%10)**2
                n = n // 10
            if count == 1:
                return True
            print(count)
            n = count
            count = 0
            times -= 1
        return False

    def isHappy(self, n: int) -> bool:          ##与上边方法一样，只是在处理跳出时的情况不同

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()                ##检查是否出现循环（也可以使用快慢指针法检测）
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1

print(Solution().isHappy(2))