'''
Minimum Swaps for Bracket Balancing
You are given a string of 2N characters consisting of N ‘[‘ brackets and N ‘]’ brackets. 
A string is considered balanced if it can be represented in the form S2[S1] where S1 and S2 are balanced strings. 
We can make an unbalanced string balanced by swapping adjacent characters. 
Calculate the minimum number of swaps necessary to make a string balanced.

Examples: 

Input  : []][][
Output : 2
First swap: Position 3 and 4
[][]][
Second swap: Position 5 and 6
[][][]
Input  : [[][]]
Output : 0
The string is already balanced.
'''
# Python3 program to count swaps required to balance string 
def swapCount(s): 
    
    # Swap stores the number of swaps required imbalance maintains the number of imbalance pair 
    swap = 0
    imbalance = 0; 
    
    for i in s:
        if i == '[':
            
            # Decrement the imbalance
            imbalance -= 1
        else:
            
            # Increment imbalance 
            imbalance += 1
            
            if imbalance > 0:
                swap += imbalance

    return swap

# Driver code 
s = "[]][]["; 
print(swapCount(s))

s = "[[][]]"; 
print(swapCount(s))
