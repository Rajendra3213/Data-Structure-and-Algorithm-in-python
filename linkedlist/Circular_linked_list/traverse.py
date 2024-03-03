# Replace ___ with your code

# create Node for linked list
class Node:
    def __init__(self,data):
        self.data =data
        self.next =None


# create the CircularLinkedList class
class CircularLinkedList:
    def __init__(self):
        # initialize the head field to None
        self.head = None

    # method to create a linked list
    def create_linked_list(self):

        # take four inputs for data
        data1 = input()
        data2 = input()
        data3 = input()
        data4 = input()

        # create four nodes 
        node1 = Node(data1)
        node2 = Node(data2)
        node3 = Node(data3)
        node4 = Node(data4)

        # set head field to the first node
        self.head = node1

        # link the nodes
        node1.next =node2
        node2.next =node3
        node3.next =node4

        # create circular linked list
        # by linking the last node back to first
        node4.next = node1

    # traverse linked list
    def traverse_linked_list(self):

        # traverse through linked list and print them
        current = self.head
        while current.next is not self.head:
            print(f"{current.data}",end=" -> ")
            current=current.next
        print(f"{current.data} -> {self.head.data}")


linked_list = CircularLinkedList()

# create linked list
linked_list.create_linked_list()

# traverse and print nodes
linked_list.traverse_linked_list()