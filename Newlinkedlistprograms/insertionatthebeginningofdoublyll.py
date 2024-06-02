'''
To insert a node at the beginning of a doubly linked list in Python, you need to follow these steps:

Create a new node with the given data.
Set the “next” pointer of the new node to point to the current head (if any).
Set the “previous” pointer of the new node to None (as it will become the new head).
If the list is not empty, update the “previous” pointer of the current head to point to the new node.
Update the head of the list to point to the new node.
'''

# Python Program for a doubly linked list at the beginning of a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Function to insert a node at the beginning of a doubly linked list
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

# Function to display the elements of the doubly linked list
def display(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")


# Driver Code
head = None
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 2)
head = insert_at_beginning(head, 1)

print("Doubly Linked List after insertion at the beginning:")
display(head)
