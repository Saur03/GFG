'''
To delete a node at a given position in a doubly linked list in Python, you need to follow these steps:

Check if the list is empty (head is None). If it is empty, there is nothing to delete.
If the position is less than 0, print an error message as it’s an invalid position.
If the position is 0, delete the node at the beginning of the list.
Traverse the list to find the node at the given position.
Update the “next” pointer of the previous node to skip the node to be deleted.
Update the “previous” pointer of the next node to point to the previous node of the node to be deleted.
Optionally, free the memory allocated to the deleted node.
'''
# Python Program for Deletion of a given node
class Node:
    def __init__(self, data):
        # Initialize a new node with data, previous, and next pointers
        self.data = data
        self.next = None
        self.prev = None


def delete_at_position(head, position):
    # Delete the node at a given position from the doubly linked list
    if head is None:
        print("Doubly linked list is empty")
        return None

    if position < 0:
        print("Invalid position")
        return head

    if position == 0:
        if head.next:
            head.next.prev = None
        return head.next

    current = head
    count = 0
    while current and count < position:
        current = current.next
        count += 1

    if current is None:
        print("Position out of range")
        return head

    if current.next:
        current.next.prev = current.prev
    if current.prev:
        current.prev.next = current.next

    del current
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

# Delete the node at position 2 (node with data 3):
head = delete_at_position(head, 2)

# Traverse and print the nodes after deletion:
traverse(head)
