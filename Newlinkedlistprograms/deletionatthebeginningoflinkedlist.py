'''
To delete a node from the beginning of a doubly linked list in Python, you need to follow these steps:

Check if the list is empty (head is None). If it is empty, there is nothing to delete.
If the list has only one node, set the head to None to delete the node.
Otherwise, update the head to point to the next node.
Set the “previous” pointer of the new head to None.
Optionally, free the memory allocated to the deleted node.
'''
# Python Program for the deletion at the beginning
class Node:
    def __init__(self, data):
        # Initialize a new node with data, previous, and next pointers
        self.data = data
        self.next = None
        self.prev = None

def delete_at_beginning(head):
    # Delete the first node from the beginning of the doubly linked list
    if head is None:
        print("Doubly linked list is empty")
        return None

    if head.next is None:
        return None

    new_head = head.next
    new_head.prev = None
    del head
    return new_head

def traverse(head):
    # Traverse the doubly linked list and print its elements
    current = head
    while current:
      # Print current node's data
        print(current.data, end=" <-> ")  
        # Move to the next node
        current = current.next  
    print("None")

def insert_at_beginning(head, data):
    # Insert a new node at the beginning of the doubly linked list
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

# Driver Code
head = None
head = insert_at_beginning(head, 4)
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 2)
head = insert_at_beginning(head, 1)
    
# Delete the first node (node with data 1) from the beginning:
head = delete_at_beginning(head)

# Traverse and print the nodes after deletion:
traverse(head)
