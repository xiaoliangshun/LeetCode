class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ""
        while n:
            res = n % 26
            if res == 0:            #为0时特殊情况的处理
                n -= 26
                s += "Z"
            else:
                s += chr(res + 64)
            # print("yushu",n%26)
            n //= 26
            # print("shang",n)
        return s[::-1]          ##倒置

#或者：
#10进制转换为26进制。本身不难，但是因为其去掉了数字0，只有1-9因而增加了难度。
# 实际上我们会发现，只要每次计算时将n先自减1（n -= 1）然后再取余数（相当于左移，此时25刚好和z对上在最高位无需特殊处理），除以26就刚好可以了。

print(Solution().convertToTitle(701))