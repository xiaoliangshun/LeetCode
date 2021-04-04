class Solution:
    def hIndex(self, citations):
        citations.sort()        ##默认从小到大排
        leng = len(citations)
        max_h = min(leng,citations[-1])             ##最大值
        for _ in range(max_h):                          ##找，（这里其实也可以使用二分法来查找，因为是有序的）
            if citations[-max_h] >= max_h:
                return max_h
            else:
                max_h -= 1
        return 0

    ## 法2 计数排序
    # 先将引用次数大于n的数变成n（因为指数最大就智能取到n：数组长度）
    # 再使用计数排序将结果放在papers数组中（n个元素记录每个出现的次数）
    # 再计算Sk填入papers[i]中：比当前元素大的个数（将papers从后向前遍历一遍）
    # 最后计算papers中min(i,papers[i])的最大值


cia = [1,8,10,3,5,18,7]
print(Solution().hIndex2(cia))