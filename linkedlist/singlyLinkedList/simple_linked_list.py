# Replace ___ with your code

# create the Node class
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        


# create the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # method to create a linked list
    def create_linked_list(self):
        # take input for node data
        data1 = int(input("Enter"))
        data2 = int(input("Enter"))
        data3 = int(input("Enter"))
        data4 = int(input("Enter"))

        # create 4 nodes with input values
        node1 = node(data1)
        node2 = node(data2)
        node1.next = node2
        node3 = node(data3)
        node2.next = node3
        node4 = node(data4)
        node3.next = node4

        # set head field to the first node
        self.head = node1

    # method to traverse and print
    def traverse_linked_list(self):
        current = self.head
        while current:
            print(f"{current.data}",end="->")
            current = current.next
        print("None")


linked_list = LinkedList()

# create a linked list
linked_list.create_linked_list()

# print the linked list
linked_list.traverse_linked_list()