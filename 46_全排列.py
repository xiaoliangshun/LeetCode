class Solution:
    def permute(self, nums):                        #有问题
        def permu(nums,count):         #count的存在使得我们不用每次检查传入的数组有多少值
            if count == 0:
                list22 = list2.copy()         #这样做就只是一个副本了
                list1.append(list22)     #######list2加入到list1，但是改变list2也会改变list1中的值
                return                  #递归返回时list1没有被返回？？？？？？？？？？？？？
            for n in nums:
                list2.append(n)
                nums1 = nums.copy()           #副本，如果用nums1 = nums 则指向的是同一个
                nums1.remove(n)
                permu(nums1,count-1)                #将递归的改变值放在递归函数值，不用再做逆操作
                list2.remove(n)
        list1 = []             #全排列
        leng = len(nums)
        list2 = []               #每一个
        permu(nums,leng)
        return list1


class Solution1:                     #参考的
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]            #没有额外的空间开销
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res

nums = [1,2,3]
print(Solution().permute(nums))

