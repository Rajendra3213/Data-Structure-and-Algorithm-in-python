# Replace ___ with your code

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self):
        data1 = int(input())
        data2 = int(input())
        data3 = int(input())

        node1 = Node(data1)
        node2 = Node(data2)
        node3 = Node(data3)

        self.head = node1
        node1.next = node2
        node2.next = node3

    # method to calculate the sum of nodes 
    def calculate_sum(self):
        sum = 0
        current =self.head
        while current:
            sum +=current.data
            current = current.next
        return sum

# create a linked list
linked_list = LinkedList()
linked_list.create_linked_list()

# calculate the sum of elements
total = linked_list.calculate_sum()
print(total)