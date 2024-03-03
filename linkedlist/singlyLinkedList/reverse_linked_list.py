# Replace ___ with your code

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # reverse linked list
    def reverse_linked_list(self):
        prev_node = None
        current_node = self.head
        next_node = current_node.next
        #sliding window techniques
        while True:
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            next_node = current_node.next

            if next_node == None:
                current_node.next = prev_node
                break
        self.head = current_node

    # traverse linked list
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

input_elements = input()
input_list = input_elements.split()

linked_list = LinkedList()
for element in input_list:
    linked_list.append(int(element))
linked_list.reverse_linked_list()
linked_list.display()