class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSubLen = 10**5
        leng = len(nums)
        for i in range(leng):                   ##从每一个元素开始向后遍历，超时O(n**2)
            count = 0
            for j in range(i,leng):
                count += nums[j]
                if count >= target:
                    minSubLen = min(minSubLen,j-i+1)
        if minSubLen == 10**5:
            return 0
        return minSubLen

    #法2：前缀和 + 二分查找
    # 创建一个数组sums用于存储nums的前缀和，其中 sums[i]表示从nums[0]到nums[i−1] 的元素和。（有了前缀和使得sum数组有序，这样就能使用二分法了）
    # 得到前缀和之后，对于每个开始下标i，可通过二分查找得到大于或等于i的最小下标bound，
    # 使得sums[bound]−sums[i−1]≥s， （减完之后就是[i-1,bound-1]之间的和）
    # 并更新子数组的最小长度（此时子数组的长度是bound−(i−1)）。


    def minSubArrayLen2(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        sums = [0]
        for i in range(n):                  ##记录前缀和
            sums.append(sums[-1] + nums[i])

        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect.bisect_left(sums, target)            ##二分查找
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))

        return 0 if ans == n + 1 else ans


    ## 法3；滑动窗口
    # 两个指针start、end 和[start,end]之间元素的和
    # 开始时都指向0，end指针后移，刷新sum，如果sum < s，就继续后移end，直到sum > s时，记录长度
    # 然后start后移一位，刷新sum,后移end，重复以上操作

    ## end指针后移是为了找到满足的条件，找到之后start开始后移--》循环，，一次就将所有可能的情况迭代完了（因为要的是最短的）
    def minSubArrayLen3(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1

        return 0 if ans == n + 1 else ans
