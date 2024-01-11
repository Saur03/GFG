'''
Given a linked list of N nodes such that it may contain a loop.
A loop here means that the last node of the link list is connected to the node at position X(1-based index). 
If the link list does not have any loop, X=0.
Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.
Example 1:
Input:N = 3
value[] = {1,3,4}
X = 2
Output: 1
Explanation: The link list looks like
1 -> 3 -> 4
     ^    |
     |____|    
A loop is present. If you remove it successfully, the answer will be 1. 

Example 2:
Input:N = 4
value[] = {1,8,3,4}
X = 0
Output: 1
Explanation: The Linked list does not contains any loop. 

Example 3:
Input:N = 4
value[] = {1,2,3,4}
X = 1
Output: 1
Explanation: The link list looks like 
1 -> 2 -> 3 -> 4
^              |
|______________|
A loop is present. If you remove it successfully, the answer will be 1. 
'''
class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        slow = head
        fast = head
        loop_exists = False

        # Detect loop using Floyd's Cycle Detection Algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                loop_exists = True
                break

        # If loop exists, find the starting point of the loop
        if loop_exists:
            slow = head
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next

            # Set the next node of the last node in the loop to None, removing the loop
            fast.next = None

        return head