class Solution:
    def containsNearbyDuplicate(self, nums, k):         #时间复杂度O(n**2)【超时】
        leng = len(nums)
        for i in range(leng):
            for j in range(i+1,i+k+1):          #和后边距离在k以内的比较
                if j < leng and nums[i] == nums[j]:
                    return True
        return False

    def containsNearbyDuplicate2(self, nums, k):        #散列表
        set1 = set()
        for i in range(len(nums)):
            if nums[i] in set1:             #判断
                return True
            if i < k:               ##前k个先放进去
                set1.add(nums[i])
            else:
                set1.add(nums[i])           ##滑动窗口，更新容器
                set1.remove(nums[i-k])
        return False


pre = [99,99]
print(Solution().containsNearbyDuplicate2(pre,2))

