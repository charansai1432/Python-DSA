
class stack:
    def __init__(self):
        self.stack = []
        
    def push(self,x):
        self.stack.append(x)
        
    def pop(self):
        if not self.stack:
            return "stack empty"
        self.stack.pop()
        
    def top(self):
        if not self.stack:
            return "stack is empty "
        self.stack[-1]
        
    def print(self):
        print(self.stack)
        
s1 = stack()
# s1.push(10)
# s1.push(20)
# s1.push(30)
# s1.push(40)
# s1.push(50)


print(s1.pop())
# s1.top()
# s1.print()