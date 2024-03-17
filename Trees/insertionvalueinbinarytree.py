'''
You are given a pointer to the root of a binary search tree and values to be inserted into the tree. 
Insert the values into their appropriate position in the binary search tree and return the root of the updated binary tree. 
You just have to complete the function.

Input Format

You are given a function,

Node * insert (Node * root ,int data) {

}
Constraints

No. of nodes in the tree <equalto 500
Output Format

Return the root of the binary search tree after inserting the value into the tree.

Sample Input

        4
       / \
      2   7
     / \
    1   3
The value to be inserted is 6.

Sample Output

         4
       /   \
      2     7
     / \   /
    1   3 6
'''
class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 


        def insert(self, val):
            #Enter you code here.
            newnode = Node(val)
            # case 1:root is NULL
            if self.root is None:
                self.root = newnode
                return
        
            cur= self.root
            # traverse using while loop
            while cur:
                #case2: value is lesser
                if val < cur.info:
                    if cur.left is None:
                        cur.left = newnode
                        return
                    cur = cur.left
                
                # case 3: value is greater
                else:
                    if cur.right is None:
                        cur.right = newnode
                        return
                    cur = cur.right 