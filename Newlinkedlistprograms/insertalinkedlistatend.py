'''
Insertion in Linked List at End

This method inserts the node at the end of the linked list. 
In this method, we create a new_node with the given data and check if the head is an empty node or not 
if the head is empty then we make the new_node as head and return 
else we make a current_node equal to the head traverse to the last node of the linked list 
and when we get None after the current_node the while loop breaks 
and insert the new_node in the next of current_node which is the last node of linked list.
'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def inserAtEnd(self, data):
	new_node = Node(data)
	if self.head is None:
		self.head = new_node
		return

	current_node = self.head
	while(current_node.next):
		current_node = current_node.next

	current_node.next = new_node
