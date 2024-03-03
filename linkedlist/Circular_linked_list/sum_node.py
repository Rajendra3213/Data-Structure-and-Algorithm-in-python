# Replace ___ with your code
# create Node for linked list
class Node:

    # initializer for the node class
    def __init__(self, data):

        # initialize data and next field
        self.data = data
        self.next = None

# create a CircularLinkedList class
class CircularLinkedList:
    def __init__(self):
        # initialize the head field to None
        self.head = None

    # method to create a linked list
    def create_linked_list(self):

        # take input for node data
        data1 = int(input())
        data2 = int(input())
        data3 = int(input())
        data4 = int(input())
        # create 4 nodes with input values
        node1 = Node(data1)
        node2 = Node(data2)
        node3 = Node(data3)
        node4 = Node(data4)
        # set head field to the first node
        self.head = node1
        # link the nodes
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = self.head


    def traverse_linked_list(self):
        current = self.head
        while current.next is not self.head:
            print(f"{current.data} -> ", end="")
            current = current.next
        print(f"{current.data} -> {self.head.data}")
        
    def compute_sum(self):
        if self.head is None:
            return 0
        
        current = self.head

        # initialize sum at 0
        total = 0
        while current.next is not self.head:
            total += current.data
            current = current.next

        total+=current.data

        return total


# create object of linked list
linked_list = CircularLinkedList()
linked_list.create_linked_list()
print(linked_list.compute_sum())