class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:            ###参考的
        count, m, prev = 0, len(flowerbed), -1
        for i in range(m):
            if flowerbed[i] == 1:
                if prev < 0:
                    count += i // 2  ##特殊情况，从头开始的
                else:
                    count += (i - prev - 2) // 2  # 正常情况
                if count >= n:
                    return True
                prev = i  # 更新

        if prev < 0:
            count += (m + 1) // 2  # 全是0
        else:
            count += (m - prev - 1) // 2  ##计算尾部

        return count >= n


class Solution:
    def canPlaceFlowers(self, flowerbed, n):            #有点问题
        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return n <= 0
            else:
                return n <= 1

        countAll = 0                #总的能插个数
        count = 0               #连续0能插的个数
        begin = 0
        while begin < len(flowerbed) and flowerbed[begin] == 0:
            begin += 1
        countAll += begin // 2               #开头的特殊处理

        end = len(flowerbed)-1
        while flowerbed[end] == 0 and end >= begin:
            end -= 1
        countAll += (len(flowerbed)-1-end) // 2          #结束的处理

        for i in flowerbed[begin:end+1]:
            if i == 0:
                count += 1
            else:
                if (count-1)//2 > 0:
                    countAll += (count-1) // 2              #(count-1)//2 表示的是连续count个0时最多能插几个花
                count = 0
        print(countAll)
        if countAll >= n:
            return True
        return False
flowerbed = [0,0]
print(Solution().canPlaceFlowers(flowerbed,1))

