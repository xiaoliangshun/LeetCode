class Solution:
    def insert(self, intervals, newInterval):
        def findIJ(inter,x):
            for i in range(len(intervals)):
                for j in range(2):
                    if intervals[i][j] >= x:            #第一个大于等于x的值
                        return i,j
            return len(intervals),len(intervals[0])         #找不到的话就是最后一个元素
        if intervals == []:
            return [newInterval]
        startI,startJ = findIJ(intervals,newInterval[0])
        endI,endJ = findIJ(intervals,newInterval[1])
        print(startI,startJ,endI,endJ)

        if endJ == 2:           #特殊情况
            if intervals[len(intervals)-1][len(intervals[0])-1] < newInterval[0]:
                intervals.append(newInterval)
            else:
                intervals[len(intervals)-1][len(intervals[0])-1] = newInterval[1]
            return intervals

        #分情况讨论
        if startI == endI:
            if startJ == endJ:   #此时不用分
                if newInterval[0] < intervals[0][0]:
                    intervals[0][0] = newInterval[0]
                return intervals
            else:
                if intervals[startI][0] > newInterval[0]:      #圈子变大了
                    intervals[startI][0] = newInterval[0]
                if intervals[endI][1] < newInterval[1]:          #圈子变大了
                    intervals[endI][1] = newInterval[1]
        else:
            if intervals[endI][0] > newInterval[1]:      #并没有包到最后一个区间
                intervals[startI][1] = newInterval[1]
                for i in range(endI-startI-1):                #删掉中间的
                    del intervals[startI+1]
            elif intervals[endI][0] == newInterval[1]:      #合并包括最后一个的区间
                intervals[startI][1] = intervals[endI][1]
                for i in range(endI - startI):
                    del intervals[startI+1]
        return intervals

class Solution:             ##
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ##对于区间
        left, right = newInterval
        placed = False
        ans = list()
        for li, ri in intervals:
            if li > right:
                # 在插入区间的右侧且无交集
                if not placed:                  #无交集情况下，在最边缘的情况
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                # 在插入区间的左侧且无交集
                ans.append([li, ri])
            else:                   #有交集，更新交集
                # 与插入区间有交集，计算它们的并集
                left = min(left, li)
                right = max(right, ri)

        if not placed:                  ##如果有交集，最后将交集的部分加入
            ans.append([left, right])
        return ans

intervals = [[1,5]]
newInterval = [0,1]
print(Solution().insert(intervals,newInterval))