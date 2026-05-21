class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.minstack == []:
            min_value = val
        else:
            min_value = min(val, self.minstack[-1])
        
        self.minstack.append(min_value)



    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

        
