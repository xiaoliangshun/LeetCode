class Solution:                                                     ###其实是一个拓扑的问题（判断有没有环）

    ##https://leetcode-cn.com/problems/course-schedule/solution/ke-cheng-biao-by-leetcode-solution/
    #法1：深度优先遍历  找到所有的分支，看是否有环
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        result = list()
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)              ##递归
                    if not valid:
                        return              ##优化
                elif visited[v] == 1:       ##有环
                    valid = False
                    return          #优化
            visited[u] = 2
            result.append(u)

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        return valid

        #法2：广度优先遍历（寻找从入度为0的节点开始）
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1             ##入度

        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])      ##队列
        visited = 0

        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses

    def canFinish3(self, numCourses, prerequisites):
        def can(a,vised):           #？？？？？有问题（我的，，判断有环否）
            for i in range(numCourses):
                if prerequisites[i][0] == a and vised[prerequisites[i][1]] == 1:        #有环
                    return False
                elif prerequisites[i][0] == a and vised[prerequisites[i][1] == 0:        #继续递归
                    vised[prerequisites[i][1]] = 1
                    return can(prerequisites[i][1],vised)
            return True
        for i in range(numCourses):
            vised = [0]*numCourses
            if not can(prerequisites[i][0]):
                return False
        return True

pre = [[1,0],[0,2],[2,1]]
print(Solution().canFinish(3,pre))

