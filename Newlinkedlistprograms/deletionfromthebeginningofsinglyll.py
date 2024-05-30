'''
To delete a node from the beginning of a singly linked list in Python, you need to follow these steps:

If the list is empty (head is None), there is nothing to delete.
Update the head of the list to point to the next node (if any).
'''
# Python Program for the deletion of a node at the beginning
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


def delete_at_beginning(head):
    # Delete the node at the beginning of the linked list
    if head is None:
        print("Error: Singly linked list is empty")
        return None

    new_head = head.next
    del head
    return new_head


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

# Delete the node at the beginning (node with data 1)
head = delete_at_beginning(head)

# Traverse and print the nodes after deletion
traverse(head)
