'''
To insert a node after a given node in a singly linked list in Python, you need to follow these steps:

Create a new node with the given data.
Set the “next” pointer of the new node to point to the next node of the given node.
Update the “next” pointer of the given node to point to the new node.
'''
# Python Program for Insertion after a given node
class Node:
    def __init__(self, data):
        # Initialize a new node with data and next pointer
        self.data = data
        self.next = None


def insert_at_beginning(head, data):
    # Insert a new node at the beginning of the linked list
    new_node = Node(data)
    new_node.next = head
    return new_node


def insert_after_node(node, data):
    # Insert a new node with given data after the specified node
    if node is None:
        print("Error: The given node is None")
        return

    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node


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
head = insert_at_beginning(head, 1)

 # Insert 2 after the node with data 1
insert_after_node(head, 2) 

# Traverse and print the nodes after insertion
traverse(head)  
