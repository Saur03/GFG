'''
Given a pointer to the root of a binary tree, print the top view of the binary tree.
The tree as seen from the top the nodes, is called the top view of the tree.

For example :

   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4
Top View : 1->2->5->6 

Complete the function  and print the resulting values on a single line separated by space.
Input Format
You are given a function,

void topView(node * root) {}
Constraints:- 1<Nodes in the tree<500  

Output Format:- Print the values on a single line separated by space.

Sample Input

   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4
Sample Output:- 1 2 5 6
'''
def topView(root):
    #Write your code here
    d = {}
    
    def traverse(root, key, level):
        if root:
            if key not in d:
                d[key] = [root, level]
            elif d[key][1] > level:
                d[key] = [root, level]
                
            traverse(root.left, key-1, level+1)
            traverse(root.right, key+1, level+1)
            
    traverse(root, 0, 0)
    for key in sorted(d):
        print(d[key][0], end = " ")  