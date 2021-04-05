# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        begin = 1
        end = n             #两边都是闭区间[begin,end]
        mid = 0
        while begin < end:
            mid = (begin+end)//2           #mid 表示中间元素
            if isBadVersion(mid):       #是错的，前边可能还有错的
                end = mid
            else:                       #是对的，错的一定在他后边
                begin = mid+1
        return begin