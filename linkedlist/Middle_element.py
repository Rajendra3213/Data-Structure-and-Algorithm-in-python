# Replace ___ with your code

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # method to append nodes
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next
        current.next = new_node

    # method to return the middle element 
    def find_middle_element(self):
        slow = self.head
        fast = self.head
        # prev_slow = None  # Keep track of the previous node for even-sized lists

        while fast is not None and fast.next is not None:
                fast = fast.next.next
                # prev_slow = slow
                slow = slow.next
        return slow.data


# create a linked list
linked_list = LinkedList()

# take inputs and convert it to a list
data_list = list(map(int, input().split()))

# append nodes from the list
for node in data_list:
    linked_list.append(node)

# get middle element's value
middle = linked_list.find_middle_element()
print(middle)