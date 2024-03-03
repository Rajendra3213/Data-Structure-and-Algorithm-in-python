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
        # take input for node data
        data1, data2, data3, data4 = map(int, input().split())

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

    # traverse linked list
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

    # method to delete the first node
    def delete_node(self):
        self.head = self.head.next


linked_list = LinkedList()

linked_list.create_linked_list()

linked_list.delete_node()

linked_list.display()
