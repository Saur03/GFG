'''
To insert a node at the end of a singly linked list in Python, you need to follow these steps:

1. Create a new node with the given data.
2. Traverse the list to find the last node.
3. Set the “next” pointer of the last node to point to the new node.
'''
# Python Program for the insertion at the end of the Singly Linked List
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


def insert_at_end(head, data):
    # Insert a new node with given data at the end of the linked list
    new_node = Node(data)
    if head is None:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next = new_node
    return head


def traverse(head):
    # Traverse the linked list and print its elements
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Driver Code
head = None
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 2)
head = insert_at_beginning(head, 1)

# Insert 4 at the end
insert_at_end(head, 4)

# Traverse and print the nodes after insertion
traverse(head)
