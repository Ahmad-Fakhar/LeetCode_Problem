class MyQueue:

    def __init__(self):
        self.Queue_in = []
        self.Queue_out = []

    def push(self, x: int) -> None:
        self.Queue_in.append(x)

    def pop(self) -> int:
        if not self.Queue_out:
            while self.Queue_in:
                self.Queue_out.append(self.Queue_in.pop())
        return self.Queue_out.pop()

    def peek(self) -> int:
        if not self.Queue_out:
            while self.Queue_in:
                self.Queue_out.append(self.Queue_in.pop())
        return self.Queue_out[-1]
        

    def empty(self) -> bool:
        return not self.Queue_in and not self.Queue_out
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()