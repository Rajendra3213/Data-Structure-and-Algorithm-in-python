# Replace ___ with your code

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        
    # write function to peek the stack's top element
    def peek(self):
        return self.stack[-1]

    # print the stack
    def print_stack(self):
        print(self.stack)

stack1 = Stack()

# take list of numbers as input
numbers = list(map(int, input().split()))

for num in numbers:
    # push each number to the stack
    stack1.push(num)

# print the stack
stack1.print_stack()

# peek the stack
top_element = stack1.peek()

# print the peeked stack
print(top_element)