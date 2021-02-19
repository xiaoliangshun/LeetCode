class Solution:
    def majorityElement(self, nums):
        star = 0
        end = len(nums)-1
        while star < end:
            if nums[star] != nums[end]:
                del nums[star]
                del nums[end]
            star += 1
            end -= 1
        print(nums)
        return nums[0]

class Solution1:
    def majorityElement(self, nums):
        nums.sort()         #先排序
        return nums[len(nums)//2]           #中间的地方一定就是
nums = [2,2,1,1,1,2,2]
print(Solution1().majorityElement(nums))