class Solution:
    def removeDuplicates(self, nums):
        flag = 0
        i = 0
        count = len(nums)
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                flag += 1       #先+1
                if flag >= 2:           #判断是否超标（2个）
                    del nums[i+1]
                    i -= 1
                    print(nums)
            else:
                count = count - (flag-1)     #总数减去超标的个数
                flag = 0
            i += 1
            print(i,count)
        print(nums)
        return count


##方法2：双指针法class Solution(object):
    def removeDuplicates(self, nums):       ##i为工作指针，j为下一个要覆盖元素的位置，

        j, count = 1, 1

        for i in range(1, len(nums)):

            if nums[i] == nums[i - 1]:
                count += 1
            else:               #说明遇到了新元素，则我们更新 count = 1，并且将该元素移动到 j 位置，并同时增加 i 和 j。
                count = 1

            if count <= 2:          #没有超过2，i，j都后移，，超过2则只有i后移
                nums[j] = nums[i]
                j += 1

        return j

nums = [1,1,1,1,2,2,3]
print(Solution().removeDuplicates(nums))