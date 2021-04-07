class Solution:
    # 法1 ： 排序+双指针
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i,j = 0,0
        list1 = list()
        leng1,leng2 = len(nums1),len(nums2)
        while i < leng1 and j < leng2:          #其中一个遍历完就结束
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if len(list1)==0 or nums1[i] != list1[-1]:
                    list1.append(nums1[i])
                i += 1
                j += 1
        return list1

    # 法2 ：计数排序 ： 先讲一个数组进行计数排序放在一个数组中，第二个数组遍历的时候顺便按照序号在计数的数组中查找即可

    # 法3 ：hash 将连个数组都放入hash表中，遍历其中一个，再在另一个hash表中查找（时间复杂度O（1））即可


    ##350. 两个数组的交集 II 只用稍微修改即可