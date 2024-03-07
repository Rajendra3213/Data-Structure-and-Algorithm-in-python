# Replace ___ with your code

# create class to represent a circular queue
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        # initialize front pointer
        self.front = 0 
        # count the number of elements in the queue
        self.count = 0 

    # create function to check if the queue is full
    # if full, return True
    def is_full(self):
        if self.count == self.size:
            return True
        else:
            False

    # create function to check if the queue is empty
    # if empty, return True
    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    # enqueue function
    # if the queue is full, return
    # else write code for enqueue and increment count
    def enqueue(self, item):
        if self.is_full():
            return
        else:
            index = (self.front + self.count)%self.size
            self.queue[index] = item
            self.count+=1

    # dequeue function
    # if the queue is empty, return
    # else write code for dequeue and decrement count
    def dequeue(self):
        if self.is_empty():
            return
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1)%self.size
            self.count -=1


    def print_queue(self):
        print(self.queue)

# initialize circular queue with size 4
queue1 = CircularQueue(4)

# take number inputs
numbers = list(map(int, input().split()))

# add each num to the queue
for num in numbers:
    queue1.enqueue(num)

queue1.print_queue()

queue1.dequeue()
queue1.dequeue()

queue1.print_queue()