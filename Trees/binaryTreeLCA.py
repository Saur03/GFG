'''
You are given pointer to the root of the binary search tree and two values v1 and v2. 
You need to return the lowest common ancestor (LCA) of v1 and v2 in the binary search tree.

Function Description
Complete the function lca in the editor below. It should return a pointer to the lowest common ancestor node of the two values given.

lca has the following parameters:
- root: a pointer to the root node of a binary search tree
- v1: a node.data value
- v2: a node.data value

Input Format
The first line contains an integer, , the number of nodes in the tree.
The second line contains  space-separated integers representing  values.
The third line contains two space-separated integers,  and .

To use the test data, you will have to create the binary search tree yourself. Here on the platform, the tree will be created for you.

Constraints
1<equal to n, node.data < equal to 25
1<equal to v1, v2< equal to 25
v1!=v2

The tree will contain nodes with data equal to v1 and v2 .
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None

      def lca(root, v1, v2):
  #Enter your code here
           if v1 > v2:
               v1, v2 = v2, v1
               
               while True:
                    if v1 < root.info and v2 < root.info:
                        root = root.left
                    elif v1 > root.info and v2 > root.info:
                         root = root.right
                    else:
                         return root           
           
