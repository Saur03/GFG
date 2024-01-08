'''
Given an array A of positive integers. 
Your task is to find the leaders in the array. An element of array is a leader if it is greater than or equal to all the elements to its right side. 
The rightmost element is always a leader. 

Example 1:
Input:
n = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: The first leader is 17 as it is greater than all the elementsto its right.  
Similarly, the next leader is 5. The right most element is always a leader so it is also included.

Example 2:
Input:
n = 5
A[] = {1,2,3,4,0}
Output: 4 0
Explanation: 0 is the rightmost elementand 4 is the only element which is greater than all the elements to its right.
'''
class Solution:
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        list = []
        max_right = A[N-1]
        for i in range(N-1, -1, -1):
            if A[i] >= max_right:
                list.append(A[i])
                max_right = A[i]

        list.reverse()
        return list
            

