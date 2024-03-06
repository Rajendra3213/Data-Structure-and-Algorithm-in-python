# Replace __ with your code

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

stack1 = Stack()

text = input()

# push characters one by one to stack1
for character in text:
    stack1.push(character)

result1 = [ ]
result = " "

while True:
    if stack1.is_empty():
        break

    # write code here
    result1.append(stack1.pop())
 
result = "".join(result1)

print(result)