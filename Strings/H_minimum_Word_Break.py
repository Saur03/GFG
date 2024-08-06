'''
Minimum Word Break
Given a string s, break s such that every substring of the partition can be found in the dictionary. 
Return the minimum break needed. 

Examples: 

Given a dictionary ["Cat", "Mat", "Ca", 
     "tM", "at", "C", "Dog", "og", "Do"]
Input :  Pattern "CatMat"
Output : 1 
Explanation: we can break the sentences
in three ways, as follows:
CatMat = [ Cat Mat ]  break 1
CatMat = [ Ca tM at ] break 2
CatMat = [ C at Mat ] break 2  so the 
         output is: 1

Input : Dogcat
Output : 1
'''
# Python program to find minimum breaks needed
# to break a string in dictionary words.

import sys


class TrieNode:

    def __init__(self):
    
        self.endOfTree = False
        self.children = [None for i in range(26)]
        


root = TrieNode()
minWordBreak = sys.maxsize

# If not present, inserts a key into the trie
    # If the key is the prefix of trie node, just
    # marks leaf node
def insert(key):

    global root,minWordBreak

    length = len(key)

    pcrawl = root

    for i in range(length):

        index = ord(key[i])- ord('a')

        if(pcrawl.children[index] == None):
            pcrawl.children[index] = TrieNode()
        pcrawl = pcrawl.children[index]
        
        # mark last node as leaf
        pcrawl.endOfTree = True

# function break the string into minimum cut
# such the every substring after breaking
# in the dictionary.
def _minWordBreak(key):

    global minWordBreak

    minWordBreak = sys.maxsize
        
    minWordBreakUtil(root, key, 0, sys.maxsize, 0)

def minWordBreakUtil(node,key,start,min_Break,level):

    global minWordBreak,root

    pCrawl = node

    # base case, update minimum Break
    if (start == len(key)):
            min_Break = min(min_Break, level - 1)
            if(min_Break<minWordBreak):
                minWordBreak = min_Break
            
            return
        

    # traverse given key(pattern)
    for i in range(start,len(key)):
        index = ord(key[i]) - ord('a')
        if (pCrawl.children[index]==None):
            return

        # if we find a condition were we can
        # move to the next word in a trie
        # dictionary
        if (pCrawl.children[index].endOfTree):
            minWordBreakUtil(root, key, i + 1,min_Break, level + 1)

        pCrawl = pCrawl.children[index]
        


# Driver code
keys=["cat", "mat", "ca", "ma", "at", "c", "dog", "og", "do" ]

for i in range(len(keys)):
    insert(keys[i])

_minWordBreak("catmatat")

print(minWordBreak)

