class Solution:
    def find132pattern(self, nums: List[int]) -> bool:      ##暴力：超时
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if nums[k] > nums[i] and nums[k] < nums[j]:
                        return True
        return False

        ##法2：枚举3（132模式的中间位置）左侧维护最小值，，右侧用平衡二叉树寻找比3小的最大值
    def find132pattern2(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        # 左侧最小值
        left_min = nums[0]
        # 右侧所有元素
        right_all = SortedList(nums[2:])

        for j in range(1, n - 1):
            if left_min < nums[j]:
                index = right_all.bisect_right(left_min)
                if index < len(right_all) and right_all[index] < nums[j]:
                    return True
            left_min = min(left_min, nums[j])
            right_all.remove(nums[j + 1])

        return False

        ##法3：枚举1  单调栈  ？？
        ##****通过维护「单调递减」来确保已经找到了有效的 (j,k),再在前边找到比k小的值即可
    def find132pattern3(self, nums: List[int]) -> bool:
        n = len(nums)
        candidate_k = [nums[n - 1]]
        max_k = float("-inf")

        for i in range(n - 2, -1, -1):     #从后向前遍历
            if nums[i] < max_k:             #max_k维护的是最后边的2
                return True                 ##一旦出现比2跟小的，就成功了
            while candidate_k and nums[i] > candidate_k[-1]:        ##保证当前栈低为更大的值
                max_k = candidate_k[-1]                 ##max_k为当前的仅次于num[i]的最大值
                candidate_k.pop()
            if nums[i] > max_k:                 ##单调栈维护的是从右到左递减的
                candidate_k.append(nums[i])

        return False