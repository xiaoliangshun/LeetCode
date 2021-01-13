class Solution:

    ###链接：https://leetcode-cn.com/problems/gray-code/solution/gray-code-jing-xiang-fan-she-fa-by-jyd/
    ##利用镜像，例如：
    #   n=0: 0
    #   n=1: 0 $$ 1                     #其实是递归的构造
    #   n=2: 00 01  $$   11 10         将n=1时的结果，像镜子一样倒着复制一份，前一半前边加0，后一半加1
    #   n=3: 000 001 011 010  $$  110 111 101 100               关键再与镜像的衔接处后边是相同的，只有第一位不同，后边的就像是倒着走前边的过程
    #   n=........
    def grayCode(self, n: int) -> List[int]:
        res, head = [0], 1
        for i in range(n):      #总循环次数，每次多一位
            for j in range(len(res) - 1, -1, -1):       ##倒着循环，才能造出镜像
                res.append(head + res[j])
            head <<= 1          ##高位的1（相当与*2）
        return res



