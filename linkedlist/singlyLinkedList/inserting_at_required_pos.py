# Replace ___ with your code

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # create linked list
    def create_linked_list(self):
        node1 = Node(8)
        self.head = node1

        node2 = Node(3)
        node1.next = node2

        node3 = Node(9)
        node2.next = node3

        node4 = Node(7)
        node3.next = node4

        node5 = Node(6)
        node4.next = node5

    # traverse linked list
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

    # insert node to linked list
    def insert_node(self, data, position):
        new_node = Node(data)
        current = self.head
        for i in range(1, position-1):
            current = current.next
        new_node.next = current.next
        current.next = new_node


linked_list = LinkedList()

# create the initial linked list
linked_list.create_linked_list()

# position of the new node
position = int(input())

# the data value of the new node
data = int(input())

linked_list.insert_node(data, position)

# print the updated linked list
linked_list.display()
