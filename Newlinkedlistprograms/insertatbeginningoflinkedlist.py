'''
Insertion at Beginning in Linked List:-

This method inserts the node at the beginning of the linked list. 
In this method, we create a new_node with the given data 
and check if the head is an empty node or not if the head is empty then we make the new_node as head 
and return else we insert the head at the next new_node and make the head equal to new_node.
'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def insertAtBegin(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
    else:
        new_node.next = self.head
        self.head = new_node
