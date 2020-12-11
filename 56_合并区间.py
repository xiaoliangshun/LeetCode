class Solution:
    def merge(self, intervals):
        intervals1 = sorted(intervals,key = lambda x:x[0])      #按照第一列排序（二位数组）##sorted(a, key=lambda x: (x[1], x[0]))  先按第二列排序，再按第一列排序
        print(intervals1)
        i = 0
        while i < len(intervals1)-1:
            print(i)
            if intervals1[i][1] >= intervals1[i+1][0] and intervals1[i][1] < intervals1[i+1][1]:        #合并
                intervals1[i][1] = intervals1[i+1][1]
                del intervals1[i+1]
                i -= 1
            elif intervals1[i][1] >= intervals1[i+1][0] and intervals1[i][1] > intervals1[i+1][1]:        #
                del intervals1[i+1]
                i -= 1
            # elif intervals1[i][0] == intervals1[i+1][0] and intervals1[i][1] >= intervals1[i+1][1]:   #多余的检查
            #     del intervals1[i+1]
            #     i -= 1
            # elif intervals1[i][0] == intervals1[i+1][0] and intervals1[i][1] < intervals1[i+1][1]:
            #     del intervals1[i]
            #     i -= 1
            elif intervals1[i][1] == intervals1[i+1][1] and intervals1[i][0] >= intervals1[i+1][0]:
                del intervals1[i]
                i -=1
            elif intervals1[i][1] == intervals1[i+1][1] and intervals1[i][0] < intervals1[i+1][0]:
                del intervals1[i+1]
                i -= 1
            i += 1
        return intervals1
##########方法2：也是先排序，然后我们设置一个输出数组merge，
# 当我们当前元素的左端点 < merge数组最后的右端点时，证明有重合-->则将merge右侧端点设置为当前右端点与原右端点的较大值
# 否则就是新的一段，将其加入数组，如此一直循环到最后

#链接：https://leetcode-cn.com/problems/merge-intervals/solution/he-bing-qu-jian-by-leetcode-solution/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged



nums = [[1,4],[2,3]]
print(Solution().merge(nums))

