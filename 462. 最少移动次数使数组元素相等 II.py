class Solution:
    def minMoves2(self, nums):        ##中位数移动次数最少
        nums.sort()
        leng = len(nums)
        sum = 0
        for i in range(leng):
            sum += abs(nums[i] - nums[leng//2])                 ##有问题：如果元素有偶数个，选择那个都可能
        return sum

    ##可以使用快排查找第leng//2大的元素             ？？？？？有问题
    def minMoves2(self, nums):
        def quick_sort(lists, i, j, targetid):  # 快排
            if i >= j:
                return list
            pivot = lists[i]
            low = i
            high = j
            while i < j:
                while i < j and lists[j] >= pivot:
                    j -= 1
                lists[i] = lists[j]
                while i < j and lists[i] <= pivot:
                    i += 1
                lists[j] = lists[i]
            lists[j] = pivot
            if j > targetid:
                return quick_sort(lists, low, i - 1, targetid)
            elif j < targetid:
                return quick_sort(lists, i + 1, high, targetid - i - 1)
            else:
                return lists[j]                                     ########??????????有问题

        leng = len(nums)
        nu = quick_sort(nums, 0, leng - 1, leng // 2)
        sum = 0
        for i in range(leng):
            sum += abs(nums[i] - nu)
        return sum
nums = [1,2,3]
print(Solution().minMoves(nums))
