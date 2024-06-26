'''
Given a team of N players. How many minimum games are required to find the second-best player?  

We can use adversary arguments based on the tournament tree (Binary Heap). 
A Tournament tree is a form of min (max) heap which is a complete binary tree. 
Every external node represents a player and the internal node represents the winner. 

In a tournament tree, every internal node contains the winner and every leaf node contains one player. 
There will be N – 1 internal node in a binary tree with N leaf (external) nodes. 

For details see this post (put n = 2 in the equation given in the post). 
It is obvious that to select the best player among N players, (N – 1) players are to be eliminated, 
i.e. we need a minimum of (N – 1) games (comparisons). 
Mathematically we can prove it. In a binary tree, I = E – 1, 
where I is a number of internal nodes and E is a number of external nodes. 
It means to find the maximum or minimum element of an array, we need N – 1 (internal nodes) comparisons. 
'''