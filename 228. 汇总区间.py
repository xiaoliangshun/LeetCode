class Solution:
    def summaryRanges(self, nums):
        if not nums:                    #特殊情况判断
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        list1 = list()
        pre = 0             #记录上一个不连续的开始
        count = 0               #记录连续的数量
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:          #i+1才是工作指针
                count += 1
            else:
                if count == 0:
                    list1.append(str(nums[pre]))
                else:
                    list1.append(str(nums[pre])+"->"+str(nums[pre]+count))
                count = 0
                pre = i+1
        if count == 0:                                              ##最后的（连续或单独）都没有加进去
            list1.append(str(nums[pre]))
        else:
            list1.append(str(nums[pre]) + "->" + str(nums[pre] + count))
        return list1

    ###官方解法
    def summaryRanges2(self, nums):         #定于low和hight，hight向后移动直到找到以low不相等的元素，若low==hight-1则只有一个元素
        list1 = list()
        i = 0
        n = len(nums)
        while i < n :
            low = i
            i += 1
            while i < n and nums[i] == nums[i - 1] + 1:         #找到了下一个不相同的元素
                i += 1
            high = i - 1            #回到最后一个相同的元素
            temp = str(nums[low])
            if low < high:
                temp += "->"
                temp += str(nums[high])
            list1.append(temp)
        return list1
print(Solution().summaryRanges2([0,1,2,4,5,7]))