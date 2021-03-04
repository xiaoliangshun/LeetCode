class MyStack:                                      ##使用两个队列模拟
    def __init__(self):
        self.queue1 = collections.deque()           ##作为出栈的栈
        self.queue2 = collections.deque()               ##放刚进来的一个元素

    def push(self, x: int) -> None:
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())       #将原来已经逆序的数排在该元素后边
        self.queue1,self.queue2 = self.queue2,self.queue1       #queue1栈作为存放元素的栈

    def pop(self) -> int:
        return self.queue1.popleft()

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1

class MyStack2:                                         ##使用一个队列模拟
    def __init__(self):
        self.queue1 = collections.deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)                   #默认右边进入
        for _ in range(len(self.queue1)-1):             ##将排在该元素前边的值都按顺序放在自己后边，保证该元素在最前边
            self.queue1.append(self.queue1.popleft())

    def pop(self) -> int:
        return self.queue1.popleft()

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1


print(Solution().maximalSquare(matri))


