'''
Find next right node of a given key.
Given a Binary tree and a key in the binary tree, find the node right to the given key. 
If there is no node on right side, then return NULL. 
Expected time complexity is O(n) where n is the number of nodes in the given binary tree.

For example, consider the following Binary Tree. Output for 2 is 6, output for 4 is 5. Output for 10, 6 and 5 is NULL. 

                  10
                /    \
              2        6
            /   \        \ 
           8     4         5
'''
# Python program to find next right node of given key

# A Binary Tree Node
class Node:
	
	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
	
# Method to find next right of a given key k, it returns
# None if k is not present in tree or k is the rightmost
# node of its level
def nextRight(root, k):

	# Base Case
	if root is None:
		return 0

	# Create an empty queue for level order traversal
	qn = [] # A queue to store node addresses
	q1 = [] # Another queue to store node levels

	level = 0

	# Enqueue root and its level
	qn.append(root)
	q1.append(level)

	# Standard BFS loop
	while(len(qn) > 0):

		# Dequeue an node from qn and its level from q1
		node = qn.pop(0)
		level = q1.pop(0)

		# If the dequeued node has the given key k
		if node.key == k :

			# If there are no more items in queue or given
			# node is the rightmost node of its level, 
			# then return None
			if (len(q1) == 0 or q1[0] != level):
				return None

			# Otherwise return next node from queue of nodes
			return qn[0]

		# Standard BFS steps: enqueue children of this node
		if node.left is not None:
			qn.append(node.left)
			q1.append(level+1)

		if node.right is not None:
			qn.append(node.right)
			q1.append(level+1)

	# We reach here if given key x doesn't exist in tree
	return None

def test(root, k):
	nr = nextRight(root, k)
	if nr is not None:
		print ("Next Right of " + str(k) + " is " + str(nr.key))
	else:
		print ("No next right node found for " + str(k))

# Driver program to test above function
root = Node(10)
root.left = Node(2)
root.right = Node(6)
root.right.right = Node(5)
root.left.left = Node(8)
root.left.right = Node(4)

test(root, 10)
test(root, 2)
test(root, 6)
test(root, 5)
test(root, 8)
test(root, 4)

