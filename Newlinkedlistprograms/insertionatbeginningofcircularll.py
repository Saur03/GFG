'''
To insert a node at the beginning of a circular linked list, you need to follow these steps:

Create a new node with the given data.
If the list is empty, make the new node the head and point it to itself.
Otherwise, set the next pointer of the new node to point to the current head.
Update the head to point to the new node.
Update the next pointer of the last node to point to the new head (to maintain the circular structure).
'''
# Python Program for the Insertion at the Beginning
class Node:
    def __init__(self, data):
        # Initialize a node with data and next pointer
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with head pointer pointing to None
        self.head = None

    def insert_at_beginning(self, data):
        # Insert a new node with data at the beginning of the linked list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        # Display the elements of the linked list
        current = self.head
        while current:
            # Traverse through each node and print its data
            print(current.data, end=" -> ")
            current = current.next
        # Print None to indicate the end of the linked list
        print("None")

# Driver Code
linked_list = LinkedList()
linked_list.insert_at_beginning(3)
linked_list.insert_at_beginning(2)
linked_list.insert_at_beginning(1)

print("Linked List after insertion at the beginning:")
linked_list.display()
