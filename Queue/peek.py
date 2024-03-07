# Replace ___ with code

class Queue:
    def __init__(self):
        self.queue = []

    # write function to check if the queue is empty
    # return True if empty
    def is_empty(self):
        if len(self.queue) == 0:
            return False
        return True

    # enqueue function
    def enqueue(self, item):
        self.queue.append(item)

    # peek function
    def peek(self):
       # if queue is not empty, peek the queue
        if self.is_empty() != False:
            return self.queue[0]

    def print_queue(self):
        print(self.queue)


# initializes queue attribute to an empty list
queue1 = Queue()

# take list of numbers as input
numbers = list(map(int, input().split()))

# enqueue each number to the queue
for num in numbers:
    queue1.enqueue(num)

# print queue
queue1.print_queue()

# peek first element of the queue
first_element = queue1.peek()

# print the peeked queue
print(first_element)
