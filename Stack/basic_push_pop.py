# Replace ___ with your code

class Stack:

    # add code to initialize, pop and push
    def __init__(self):
        self.stack = []

    # create function for push
    def push(self, item):
        self.stack.append(item)

    # create function for pop 
    def pop(self):
        self.stack.pop()
        # print(item)
        


    # print the stack
    def print_stack(self):
        print(self.stack)

# initializes stack attribute to an empty list
stack1 = Stack()

# take list of numbers as input
numbers = list(map(int, input().split()))

# push each number to the stack
for num in numbers:
    # push num to stack
    stack1.push(num)

# print the stack
stack1.print_stack()

# remove an item
stack1.pop()

# print the stack
stack1.print_stack()

# remove another item
stack1.pop()

# print the stack
stack1.print_stack()