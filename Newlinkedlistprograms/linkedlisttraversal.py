'''
Linked List Traversal in Python

This method traverses the linked list and prints the data of each node. 
In this method, we made a current_node equal to the head and iterate through the linked list using a while loop 
until the current_node become None and print the data of current_node in each iteration 
and make the current_node next to it.
'''
def printLL(self):
	current_node = self.head
	while(current_node):
		print(current_node.data)
		current_node = current_node.next
