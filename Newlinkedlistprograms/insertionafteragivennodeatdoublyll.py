'''
To insert a node after a given node in a doubly linked list in Python, you can follow these steps:

Create a new node with the given data.
Set the “next” pointer of the new node to point to the next node of the given node.
Set the “previous” pointer of the new node to point to the given node.
If the next node of the given node is not None, update the “previous” pointer of that node to point to the new node.
Update the “next” pointer of the given node to point to the new node.
'''
# Python Program for Insertion after a given node 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Function to insert a node after a given node in a doubly linked list
def insert_after_node(node, data):
    if node is None:
        print("Error: The given node is None")
        return

    new_node = Node(data)
    new_node.prev = node
    new_node.next = node.next

    if node.next:
        node.next.prev = new_node

    node.next = new_node

# Function to display the elements of the doubly linked list
def display(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")


# Driver Code
head = Node(1)
node2 = Node(2)
node3 = Node(3)

head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2

print("Doubly Linked List before insertion:")
display(head)

insert_after_node(node2, 4)

print("Doubly Linked List after insertion:")
display(head)
