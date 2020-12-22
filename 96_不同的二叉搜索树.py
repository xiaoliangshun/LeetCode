class Solution:
    def numTrees(self, n):              #不会-----------动态规划法
            #给定一个有序序列n1⋯n，为了构建出一棵二叉搜索树，我们可以遍历每个数字i，
            # 将该数字作为树根，将1⋯(i−1) 序列作为左子树，将(i+1)⋯n 序列作为右子树。接着我们可以按照同样的方式递归构建左子树和右子树
            #G(n) =  i=1~n∑ G(i−1)⋅G(n−i)
# 链接：https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode-solution/

        G = [0] * (n + 1)
        G[0], G[1] = 1, 1

        for i in range(2, n + 1):           #i就是我们计算的n
            for j in range(1, i + 1):               #j为计算过程总用到的
                G[i] += G[j - 1] * G[i - j]             #用的是前边的计算结果

        return G[n]

    #法2：数学推倒