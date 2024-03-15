'''
For the purposes of this challenge, we define a binary tree to be a binary search tree with the following ordering requirements:

The data value of every node in a node's left subtree is less than the data value of that node.
The data value of every node in a node's right subtree is greater than the data value of that node.
Given the root node of a binary tree, can you determine if it's also a binary search tree?

Complete the function in your editor below, which has 1 parameter: a pointer to the root of a binary tree. It must return a boolean denoting whether or not the binary tree is a binary search tree. You may have to write one or more helper functions to complete this challenge.

Input Format
You are not responsible for reading any input from stdin. 
Hidden code stubs will assemble a binary tree and pass its root node to your function as an argument.

Constraints
0<equal to data <equal to 100000
'''
def check_binary_search_tree_(root):
    #create a helper function
    def check(root, min_value, max_value):
        # base case
        if root is None:
            return True
        
        # check general case
        if root.data < min_value or root.data > max_value:
            return False
        
        return check(root.left, min_value, root.data-1) and check(root.right, root.data+1, max_value)
    
    return check(root, 0, 100000)