class MyStack:

    def __init__(self):
        self.p1=deque()
        self.p2=deque()
    def push(self, x: int) -> None:
        self.p2.append(x)
        while self.p1:
            self.p2.append(self.p1.popleft())
        self.p1,self.p2=self.p2,self.p1
    def pop(self) -> int:
        return self.p1.popleft()
    def top(self) -> int:
        return self.p1[0]
    def empty(self) -> bool:
        return len(self.p1)==0
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()