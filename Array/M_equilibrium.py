'''
Given an array A of n non negative numbers. The task is to find the first equilibrium point in an array. 
Equilibrium point in an array is an index (or position) such that the sum of all elements before that index is same as sum of elements after it.
Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists. 

Example 1:
Input: 
n = 5 
A[] = {1,3,5,2,2} 
Output: 
3 
Explanation:  equilibrium point is at position 3 as sum of elements before it (1+3) = sum of elements after it (2+2). 

Example 2:
Input:
n = 1
A[] = {1}
Output: 
1
Explanation:vSince there's only element hence its only the equilibrium point.
Your Task:
The task is to complete the function equilibriumPoint() which takes the array and n as input parameters and returns the point of equilibrium.
'''
class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        if N == 1:
            return 1
    
        total_sum = sum(A)
        left_sum = 0
        right_sum = total_sum
    
        for i in range(N):
            right_sum -= A[i]
        
            if left_sum == right_sum:
                return i + 1
        
            left_sum += A[i]
    
        return -1