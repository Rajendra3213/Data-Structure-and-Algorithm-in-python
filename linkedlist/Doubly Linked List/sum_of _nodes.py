class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Add a reference to the previous node
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def create_linked_list(self):
        data = list(map(int, input().split()))
        nodes = [Node(i) for i in data]

        # Connect nodes in both forward and backward directions
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
            nodes[i + 1].prev = nodes[i]

        self.head = nodes[0]

    def compute_sum(self):
        current = self.head
        total_sum = 0

        while current is not None:
            total_sum += current.data
            current = current.next

        return total_sum

# Create an object of the doubly linked list
linked_list = DoublyLinkedList()

# Input space-separated integers to create the linked list
linked_list.create_linked_list()

# Print the sum of the elements in the doubly linked list
print(linked_list.compute_sum())
