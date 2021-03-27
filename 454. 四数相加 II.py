class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count = 0                   #暴力：【超时】
        A.sort()
        B.sort()
        C.sort()
        D.sort()
        for i in range(len(A)):
            for j in range(len(B)):
                for k in range(len(C)):
                    for l in range(len(D)):
                        sum = A[i] + B[j] + C[k] + D[l]
                        if sum == 0:
                            count += 1
                        elif sum > 0:
                            break
        return count

    def fourSumCount2(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # 两次双重 for循环，   将每次的循环限制在两个数组之中，较好的降低了时间复杂度
        # 思想：降低搜索空间（与归并算法类似），，时间复杂度变成了log2 n**4 = n**2
        countAB = collections.Counter(u + v for u in A for v in B)          # 字典（key：a+b的值 ； value：个数）
        ans = 0
        for u in C:
            for v in D:
                if -u - v in countAB:                   # 同样计算（c+d的个数 使之与a+b的和为0 ）
                    ans += countAB[-u - v]
        return ans
