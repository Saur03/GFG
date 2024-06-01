'''
To delete a node at the end of a singly linked list in Python, you need to follow these steps:

1. Check if the list is empty (head is None) or if the list has only one node (i.e., head.next is None).
If either condition is true, there is nothing to delete.

2.Traverse the list to find the second-to-last node.
3. Set the “next” pointer of the second-to-last node to None to remove the last node.

4.Optionally, free the memory allocated to the deleted node.
'''
# Python Program for deletion at the End of Singly Linked List
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


def delete_at_end(head):
    # Delete the last node of the linked list
    if head is None or head.next is None:
        print("Error: Singly linked list is empty or has only one node")
        return None

    current = head
    while current.next.next:
        current = current.next

    del_node = current.next
    current.next = None
    del del_node

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
head = insert_at_beginning(head, 4)
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 2)
head = insert_at_beginning(head, 1)

# Delete the last node (node with data 4)
head = delete_at_end(head)

# Traverse and print the nodes after deletion
traverse(head)
