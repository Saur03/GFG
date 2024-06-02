'''
To insert a node at the end of a doubly linked list in Python, you need to follow these steps:

Create a new node with the given data.
If the list is empty (head is None), make the new node the head of the list.
Otherwise, traverse the list to find the last node.
Set the “next” pointer of the last node to point to the new node.
Set the “previous” pointer of the new node to point to the last node.
Optionally, update the head of the list to point to the new node if it’s the first node in the list.
'''
# Python Program for Insertion at the end
class Node:
    def __init__(self, data):
        # Initialize a new node with data, previous, and next pointers
        self.data = data
        self.next = None
        self.prev = None


def insert_at_end(head, data):
    # Insert a new node at the end of the doubly linked list
    new_node = Node(data)
    if head is None:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next = new_node
    new_node.prev = current
    return head


def display(head):
    # Display the doubly linked list elements
    current = head
    while current:
      # Print current node's data
        print(current.data, end=" <-> ")
        # Move to the next node
        current = current.next
    print("None")


# Driver Code
head = None
head = insert_at_end(head, 1)
head = insert_at_end(head, 2)
head = insert_at_end(head, 3)

print("Doubly Linked List after insertion at the end:")
display(head)
