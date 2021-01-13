class Solution:
                                ##########在46题的基础上加了去重
    def permuteUnique(self, nums):

        def unique(nums):  ##清除数组中重复的元素
            i = 0
            while i < len(nums):
                j = i + 1
                while j < len(nums):
                    if nums[i] == nums[j]:
                        del nums[j]
                        j -= 1
                    j += 1
                i += 1
            return nums

        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):           ##从first到最后
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)            #每一位都有n-first种分枝
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        res = []
        n = len(nums)
        backtrack(0)
        return unique(res)


nums=[1,2,3]
print(Solution().permuteUnique(nums))


# class Solution {                              ###优化的方法，，java代码
# boolean[] vis;          ##标记数组：记录下标的元素是否被访问过
#
# public List < List < Integer >> permuteUnique(int[] nums) {
# List < List < Integer >> ans = new ArrayList < List < Integer >> ();      #结果
# List < Integer > perm = new ArrayList < Integer > ();                     ##结果之一
# vis = new boolean[nums.length];
# Arrays.sort(nums);        #排序--》这样的话相同位置的元素就不用重复放后边一样的值了
# backtrack(nums, ans, 0, perm);
#
# return ans;
# }
#
# public void backtrack(int[] nums, List <List<Integer>> ans, int idx, List <Integer> perm) {
# if (idx == nums.length) {             ##出口
# ans.add(new ArrayList < Integer > (perm));
# return;
# }
# for (int i = 0; i < nums.length; ++i) {
#     if (vis[i] | | (i > 0 & & nums[i] == nums[i - 1] & & !vis[i - 1])) {          #可以剪枝
#     continue;
#     }
#     perm.add(nums[i]);
#     vis[i] = true;
#     backtrack(nums, ans, idx + 1, perm);
#     vis[i] = false;               ##回溯1
#     perm.remove(idx);              ##回溯2
#     }
#     }
#     }


