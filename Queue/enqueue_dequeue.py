# Replace ___ with your code

class Queue:
    def __init__(self):
        self.queue = []

    # create function for enqueue
    def enqueue(self, item):
        self.queue.append(item)
    
    # create function for dequeue
    def dequeue(self):
        self.queue.pop(0)

    def print_queue(self):
        print(self.queue)

# initializes queue attribute to an empty list
queue1 = Queue()

# take list of numbers as input
numbers = list(map(int, input().split()))

for num in numbers:
    # add each input to the queue
    queue1.enqueue(num)

# print queue
queue1.print_queue()

# remove first item of the queue
queue1.dequeue()

# print queue   
queue1.print_queue()

# remove second oldest item
queue1.dequeue()

# remove another item from updated queue
queue1.print_queue()