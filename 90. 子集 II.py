class Solution:
    def subsetsWithDup(self, nums) :                        ######我的：有问题？?????
        def unique(nums):  ##清除数组中重复的元素
            i = 0
            while i < len(nums):
                j = i + 1
                while j < len(nums):
                    if set(nums[i]) == set(nums[j]) and len(nums[i]) == len(nums[j]):    ##有问题的：遇到[1,1,2] [1,2,2]应该是不同的
                        del nums[j]
                        j -= 1
                    j += 1
                i += 1
            return nums

        ans = []
        temp = []
        leng = len(nums)
        def subset(temp,first):
            if first == leng:       #出口
                ans.append(temp[:])
                return
            temp.append(nums[first])
            subset(temp,first+1)        ##两种情况(总2**n种)：1.有这个元素  2.无此元素    但是要去重
            temp.remove(nums[first])
            subset(temp,first+1)
            return ans
        subset(temp,0)
        print(ans)
        return unique(ans)

        ##链接：：https://leetcode-cn.com/problems/subsets-ii/solution/90-zi-ji-iiche-di-li-jie-zi-ji-wen-ti-ru-he-qu-zho/
    # class Solution:
    #     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #         if not nums: return []
    #         res = []
    #         used = [0] * len(nums)            ##可以被下边的一个判断代替，，，同一树层上重复取x 就要过滤掉，同一树枝上就可以重复取x
    #
    #         def backtracking(nums, path, used, idx):
    #             res.append(path.copy())
    #             for i in range(idx, len(nums)):
    #                 if nums[i] == nums[i - 1] and i > 0 and not used[i - 1]:
    #                     continue
    #                 path.append(nums[i])
    #                 used[i] = 1
    #                 backtracking(nums, path, used, i + 1)
    #                 used[i] = 0
    #                 path.pop()
    #
    #         # 别忘了将nums排序
    #         backtracking(sorted(nums), [], used, 0)
    #         return res
    #######优化   去掉了used[]数组
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = []

        def backtracking(nums, path, idx):
            res.append(path.copy())
            for i in range(idx, len(nums)):                     #遍历
                if nums[i] == nums[i - 1] and i > idx:
                    continue
                path.append(nums[i])
                backtracking(nums, path, i + 1)
                path.pop()          #回溯

        # 别忘了将nums排序
        backtracking(sorted(nums), [], 0)
        return res

    ######解法3： 迭代法
    # []的所有子串[]                     与镜像颇为相似，，每次都是在上此的基础上*2，后半部分加上了新的元素
    # [1]的所有子串[]  [1]
    # [1 2]的所有子串[][1]  [2][12]
    # [1 2 3]的所有子串[][1][2][12]   [3][13][23][123]
nums = [1,1,2,2]
print(Solution().subsetsWithDup(nums))
