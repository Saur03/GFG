'''
To delete the node at the beginning of a circular linked list in Python, you need to follow these steps:

Check if the list is empty. If it is empty, there is nothing to delete.
If the list has only one node, set the head to None to delete the node.
Otherwise, find the last node of the list (the node whose next pointer points to the head).
Update the next pointer of the last node to point to the second node (head’s next).
Update the head to point to the second node.
Optionally, free the memory allocated to the deleted node.
'''
# Python Program of Deletion at the beginning of the circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
          
            # If the list is empty, make the new node point to itself
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            
            # Make the new node point back to the head
            new_node.next = self.head

    def delete_at_beginning(self):
        if not self.head:
            print("Circular Linked List is empty")
            return

        # If there is only one node in the list
        if self.head.next == self.head:
            self.head = None
            return

        current = self.head
        while current.next != self.head:
            current = current.next
            
        # Update the last node to point to the second node
        current.next = self.head.next
        
        # Update the head to point to the second node
        self.head = self.head.next

    def display(self):
        if not self.head:
            print("Circular Linked List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
            print("", end="")


# Driver Code
circular_list = CircularLinkedList()
circular_list.append(1)
circular_list.append(2)
circular_list.append(3)

print("Circular Linked List before deletion:")
circular_list.display()
print()

circular_list.delete_at_beginning()

print("Circular Linked List after deletion at the beginning:")
circular_list.display()
