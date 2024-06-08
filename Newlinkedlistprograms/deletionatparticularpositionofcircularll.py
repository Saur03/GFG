'''
To delete a node at a particular position of a circular linked list in Python, you need to follow these steps:

Check if the list is empty. If it is empty, there is nothing to delete.
If the position is 0, it means deleting the head node. In this case, update the next pointer of the last node to point to the second node and update the head.
Traverse the list to find the node at the desired position (index – 1).
Update the next pointer of the current node to skip the node to be deleted (pointing to the next node of the node to be deleted).
Optionally, free the memory allocated to the deleted node.
'''

# Python Program for Deletion at a particular position in Circular Linked List
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
            # Pointing back to itself
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            # Pointing back to the head
            new_node.next = self.head

    def delete_at_position(self, position):
        if not self.head:
            print("Circular Linked List is empty")
            return
        if position < 0:
            print("Invalid position")
            return

        # Deleting the head node
        if position == 0:

                # Only one node in the list
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return
        current = self.head
        count = 0
        while count < position - 1 and current.next != self.head:
            current = current.next
            count += 1
        if count < position - 1:
            print("Position out of range")
            return
        current.next = current.next.next

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

circular_list.delete_at_position(1)

print("Circular Linked List after deletion at position 1:")
circular_list.display()
