'''
Get Length of a Linked List in Python

This method returns the size of the linked list. 
In this method, we have initialized a counter ‘size’ with 0, and then if the head is not equal to None 
we traverse the linked list using a while loop and increment the size with 1 in each iteration 
and return the size when current_node becomes None else we return 0.
'''
def sizeOfLL(self):
	size = 0
	if(self.head):
		current_node = self.head
		while(current_node):
			size = size+1
			current_node = current_node.next
		return size
	else:
		return 0
