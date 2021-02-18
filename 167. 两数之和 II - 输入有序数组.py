class Solution:
    def twoSum(self, numbers, target):      ##双指针法
        star = 0
        end = len(numbers)-1
        while star < end:
            if numbers[star] + numbers[end] < target:       #缩小范围
                star += 1
            elif numbers[star] + numbers[end] > target:
                end -= 1
            else:
                return [star+1,end+1]
    ##二分查找：先确定一个数，用目标数字减去当前数字，此时用二分查找
nums = [2,3,4]
print(Solution().twoSum(nums,5))