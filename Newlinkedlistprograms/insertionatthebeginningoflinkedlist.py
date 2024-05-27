'''
 Insertion at the Beginning of the linked list:
To insert a node at the beginning of a singly linked list in Python, you need to follow these steps:

Create a new node with the given data.
Set the “next” pointer of the new node to point to the current head of the list.
Update the head of the list to point to the new node.
'''
# Python Program for the insertion of node at the beginning
class Node:
    def __init__(self, data):
        # Initialize a new Node with data and next pointer
        self.data = data
        self.next = None


def insert_at_beginning(head, data):
    # Insert a new node at the beginning of the linked list
    new_node = Node(data)
    new_node.next = head
    return new_node


def traverse(head):
    # Traverse the linked list and print its elements
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Driver Code
head = None
head = insert_at_beginning(head, 4)
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 2)
head = insert_at_beginning(head, 1)
traverse(head)
