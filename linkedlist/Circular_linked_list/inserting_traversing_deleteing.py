# create Node for linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create a Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return  self.head is None

    def traverse_list(self):
        if self.is_empty():
            print('Empty Linked List')
            return
        current = self.head
        while current.next is not self.head:
            print(f"{current.data} ->", end=" ")
            current = current.next
        print(f"{current.data} -> {self.head.data}")

    def node_count(self):
        if self.is_empty():
            return 0
        count = 1
        current = self.head
        while current.next is not self.head:
            count += 1
            current = current.next
        return count

    def append_into_empty(self, data):
        new_node = Node(data)
        self.head = new_node
        new_node.next = self.head

    def append(self, data):
        if self.is_empty():
            self.append_into_empty(data)
            return
        new_node = Node(data)
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
    

    def insert_at_beginning(self, data):
        if self.is_empty():  
            self.append_into_empty(data)
            return      
        new_node = Node(data)
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, data, position):
        if position <= 0 or position > self.node_count() + 1:
            print("Invalid position")
            return
        elif position == 1:
            self.insert_at_beginning(data)
            return
        elif position == self.node_count() + 1:
            self.append(data)
            return
        else:
            new_node = Node(data)
            current = self.head
            for i in range(1, position-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
    # delete from beginning
    def delete_from_beginning(self):
        if self.is_empty():
            print('Cannot delete from Empty List')
        elif self.node_count() == 1:
            temp = self.head
            self.head = None
            del temp
        else:
            temp = self.head
            current = self.head
            while current.next is not self.head:
                current = current.next
            self.head = self.head.next
            current.next = self.head
            del temp

    def delete_at_position(self, position):
        if self.is_empty():
            print('Cannot delete from Empty circular linked list')
        elif position <= 0 or position > self.node_count():
            print('Invalid position')
        elif position == 1:
            self.delete_from_beginning()
        else:
            current = self.head
            prev_node = None
            for i in range(1, position):
                prev_node = current
                current = current.next
            prev_node.next = current.next
            del current

linked_list = CircularLinkedList()
linked_list.insert_at_beginning(3)
linked_list.append(8) 
linked_list.append(9)
linked_list.insert_at_position(7, 2) 
linked_list.traverse_list()
linked_list.delete_at_position(3)
linked_list.delete_from_beginning()
linked_list.traverse_list()