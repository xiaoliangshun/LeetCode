class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x1 = x
        list1 = list()
        while x1:               ##分别用数组存储
            list1.append(x1 % 2)
            x1 = x1 // 2
        y1 = y
        list2 = list()
        while y1:
            list2.append(y1 % 2)
            y1 = y1 // 2
        lengx = len(list1)
        lengy = len(list2)
        min1 = min(lengx,lengy)
        count = 0
        for i in range(min1):           #按位对比
            if list1[i] != list2[i]:
                count += 1
        if lengx > lengy:
            for i in range(lengx - lengy):
                if list1[i+min1] == 1:
                    count += 1
        else:
            for i in range(lengy - lengx):
                if list2[i+min1] == 1:
                    count += 1
        return count


    def hammingDistance2(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')                    ##异或后计算1的个数


    def hammingDistance3(self, x, y):
        xor = x ^ y                 ##异或后一位一位查看
        distance = 0
        while xor:
            if xor & 1:
                distance += 1
            xor = xor >> 1
        return distance

    def hammingDistance4(self, x, y):
        xor = x ^ y
        distance = 0
        while xor:              ##做异或后，
            distance += 1
            # remove the rightmost bit of '1'
            xor = xor & (xor - 1)               ##x与x-1与后的结果，就是去除了最低位的1（将其变成0）
        return distance

