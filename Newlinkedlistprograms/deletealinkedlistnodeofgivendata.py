'''
Delete a Linked List Node of a given Data

This method removes the node with the given data from the linked list. 
In this method, firstly we made a current_node equal to the head and run a while loop to traverse the linked list. 
This while loop breaks when current_node becomes None or the data next to the current node is equal to the data given in the argument. 
Now, After coming out of the loop if the current_node is equal to None it means 
that the node is not present in the data and we just return, 
and if the data next to the current_node is equal to the data given 
then we remove that node by making next of that removed_node to the next of current_node. 
And this is implemented using the if else condition.
'''
def remove_node(self, data):
	current_node = self.head

	# Check if the head node contains the specified data
	if current_node.data == data:
		self.remove_first_node()
		return

	while current_node is not None and current_node.next.data != data:
		current_node = current_node.next

	if current_node is None:
		return
	else:
		current_node.next = current_node.next.next
