class Solution:
    def merge(self, nums1, m, nums2, n) -> None:

        work = m+n-1            #nums1数组的结尾
        n1 = m-1            #nums1上的工作指针
        n2 = n-1            #nums2上的工作指针
        while n1 >= 0 and n2 >= 0:          ##只要n1,n2一个没结束
            if nums1[n1] > nums2[n2]:
                nums1[work] = nums1[n1]
                n1 -= 1
            else:
                nums1[work] = nums2[n2]
                n2 -= 1
            work -= 1
        nums1[:n2 + 1] = nums2[:n2 + 1]         ##nums1可能比较短，先结束了，nums2没有结束
        return nums1
nums1 = [0]
m = 0
nums2 = [1]
n = 1
print(Solution().merge(nums1,m,nums2,n))
