class Solution:
    def addBinary(self, a, b) -> str:          ##位运算
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

    ##法2，也可以使用最普通的模拟：最低位相加带上进位