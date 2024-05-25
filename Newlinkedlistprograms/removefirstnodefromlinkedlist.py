'''
Delete Node in a Linked List

Remove First Node from Linked List
This method removes the first node of the linked list simply by making the second node head of the linked list.
'''
def remove_first_node(self):
	if(self.head == None):
		return
	
	self.head = self.head.next
