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
        node1 = Node(90)
        self.head = node1

        node2 = Node(80)
        node1.next = node2

        node3 = Node(60)
        node2.next = node3

        node4 = Node(50)
        node3.next = node4

    # traverse linked list
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

    # count elements
    def count_elements(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    # method to delete the node
    def delete_node(self, position):
        current = self.head
        if (position == 1):
            self.head = self.head.next
        for i in range(1, position-1):
            current = current.next
        current.next = current.next.next


linked_list = LinkedList()
linked_list.create_linked_list()

# the position of the new node
position = int(input())

# delete the linked list at the give position
linked_list.delete_node(position)
linked_list.display()
