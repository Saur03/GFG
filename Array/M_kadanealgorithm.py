'''
Given an array Arr[] of N integers. 
Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.
'''
from sys import maxint
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        max_so_far = -maxint - 1
        max_ending_here = 0
 
        for i in range(0, N):
            max_ending_here = max_ending_here + arr[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here
 
            if max_ending_here < 0:
                max_ending_here = 0
        
        return max_so_far
    

    
            
