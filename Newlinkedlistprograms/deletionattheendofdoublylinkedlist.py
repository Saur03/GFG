'''
To delete a node at the end of a doubly linked list in Python, you need to follow these steps:

Check if the list is empty (head is None). If it is empty, there is nothing to delete.
If the list has only one node, set the head to None to delete the node.
Traverse the list to find the last node.
Set the “next” pointer of the second-to-last node to None.
Optionally, free the memory allocated to the deleted node.
'''
# Python Program Deletion at the end
class Node:
    def __init__(self, data):
        # Initialize a new node with data, previous, and next pointers
        self.data = data
        self.next = None
        self.prev = None

def delete_at_end(head):
    # Delete the last node from the end of the doubly linked list
    if head is None:
        print("Doubly linked list is empty")
        return None

    if head.next is None:
        return None

    current = head
    while current.next.next:
        current = current.next

    del_node = current.next
    current.next = None
    del del_node
    return head

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

# Delete the last node (node with data 4) from the end:
head = delete_at_end(head)

# Traverse and print the nodes after deletion:
traverse(head)
