class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):       #我的散列表【超时】，，最笨的线性查找要O（n**2）时间复杂度
        list1 = list()
        for i in range(len(nums)):
            list1.append([i,nums[i]])               #下标与元素存在一起
        list1.sort(key=lambda x: x[1], reverse=False)   # 按列表中，每一个元组的第二个元素从小到大排序（带着下标一起排序）******

        # print(list1)
        for i in range(len(nums)-1):        #然后如果相连两个的数值差小于等于t，则对比下标若小于等于k则返回True
            for j in range(i+1,len(nums)):
                print(i,j)
                if list1[j][1] - list1[i][1] <= t and abs(list1[j][0] - list1[i][0]) <= k:
                    return True
                elif list1[j][1] - list1[j][1] <= t:            #若下标元素的差大于k，但是元素的绝对值小于等于t，可以继续往后试
                    continue
                else:           #元素差大于t，不再比较了
                    break
        return False

        ##方法二 （桶） 【通过】
        #计算nums[i] 与 t+1 相除的商，将相同的商他们放在同一个桶中，如果这个当前元素与t+1相除的结果在桶，则存在
        ##关于k相邻，其实是维护桶内刚好是k个元素（其实就是滑动窗口哦）
    def containsNearbyAlmostDuplicate2(self, nums, k, t):
        def getID(a,b):
            return a // b
        if k < 0 or t < 0:
            return False
        dict1 = dict()
        for i in range(len(nums)):
            m = getID(nums[i],t+1)      ##桶中有t+1个元素，即使一个在开头一个在最后，差距也是t
            if m in dict1:            #存在一个桶中的元素
                return True
            if m-1 in dict1 and abs(nums[i] - dict1[m-1]) < t+1:        #相邻桶
                return True
            if m+1 in dict1 and abs(nums[i] - dict1[m+1]) < t+1:
                return True
            dict1[m] = nums[i]
            if i >= k:                              ##其实是维持k+1个桶
                dict1.pop(getID(nums[i-k],t+1))         ##一个桶中只会有一个元素，直接删掉桶
        return False

        #方法三 （二叉搜索树） 【通过】   没看懂

print(Solution().containsNearbyAlmostDuplicate2([1,2,3,1],3,0))


