'''
To insert a node at the end of a circular linked list, you need to follow these steps:

1. Create a new node with the given data.
2. If the list is empty, make the new node the head and point it to itself.
3. Otherwise, traverse the list to find the last node.
4. Set the next pointer of the last node to point to the new node.
5. Set the next pointer of the new node to point back to the head (to maintain the circular structure).
'''
# Python Program for Insertion at the End
class Node:
    def __init__(self, data):
        # Initialize a node with data and next pointer
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with head pointer pointing to None
        self.head = None

    def append(self, data):
        # Append a new node with data to the end of the linked list
        new_node = Node(data)
        if not self.head:
            # If the linked list is empty, make the new node the head
            self.head = new_node
            return
        current = self.head
        while current.next:

            # Traverse the linked list until the last node
            current = current.next

        # Assign the new node as the next node of the last node
        current.next = new_node

    def display(self):

        # Display the elements of the linked list
        current = self.head
        while current:

            # Traverse through each node and print its data
            print(current.data, end=" -> ")
            current = current.next

        # Print None to indicate the end of the linked list
        print("None")


# Driver Code
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print("Linked List after insertion at the end:")
linked_list.display()
