'''
Remove Last Node from Linked List

In this method, we will delete the last node. 
First, we traverse to the second last node using the while loop, 
and then we make the next of that node None and last node will be removed.
'''
def remove_last_node(self):

	if self.head is None:
		return

	current_node = self.head
	while(current_node.next.next):
		current_node = current_node.next

	current_node.next = None
