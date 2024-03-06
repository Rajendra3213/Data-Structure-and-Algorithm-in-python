# Replace ___ with your code
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # create doubly linked list
    def create_linked_list(self):
        
        # take four inputs
        data1 = int(input())
        data2 = int(input())
        data3 = int(input())
        data4 = int(input())

        # create four nodes
        node1 = Node(data1)
        node2 = Node(data2)
        node3 = Node(data3)
        node4 = Node(data4)
        
        # set head and tail
        self.head = node1
        self.tail =node4

        # link the nodes
        node1.next = node2
        node2.prev = node1
        node2.next = node3
        node3.prev = node2
        node3.next = node4
        node4.prev = node3

    # traverse the linked list
    def traverse(self):
        current = self.head
        print("None <-> ", end="")
        # loop until the node is None
        while current is not None:
             print(f"{current.data} <-> ", end="")
             current = current.next
        print("None")

linked_list = DoublyLinkedList()
linked_list.create_linked_list()
linked_list.traverse()