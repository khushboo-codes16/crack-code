class Stack:
    def __init__(self, size):
        self.stack = []
        self.max_size = size
    
    def push(self, value):
        if len(self.stack) >= self.max_size:
            print("stack overflow")
        else:
            self.stack.append(value)
    
    def pop(self):
        if not self.stack:
            print("stack underflow")
        else:
            print(self.stack.pop())
    
    def top(self):
        if not self.stack:
            print("stack underflow")
        else:
            print(self.stack[-1])

def main():
    t = int(input())  # Number of test cases
    
    for _ in range(t):
        n, s = map(int, input().split())  # Number of commands and max stack size
        stack = Stack(s)
        
        for _ in range(n):
            command = input().split()
            if command[0] == "push":
                stack.push(int(command[1]))
            elif command[0] == "pop":
                stack.pop()
            elif command[0] == "top":
                stack.top()

if __name__ == "__main__":
    main()
