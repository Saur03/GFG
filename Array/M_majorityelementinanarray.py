'''
Given an array A of N elements. Find the majority element in the array. 
A majority element in an array A of size N is an element that appears strictly more than N/2 times in the array.

Example 1:
Input:
N = 3 
A[] = {1,2,3} 
Output:
-1
Explanation: Since, each element in {1,2,3} appears only once so there is no majority element.

Example 2:
Input:
N = 5 
A[] = {3,1,3,3,2} 
Output:
3
Explanation: Since, 3 is present more than N/2 times, so it is the majority element.
'''
class Solution:
    def majorityElement(self, A, N):
        element_count = {}
        
        # Count the occurrences of each element
        for num in A:
            if num in element_count:
                element_count[num] += 1
            else:
                element_count[num] = 1
        
        # Check for the majority element
        for key, value in element_count.items():
            if value > N // 2:
                return key
        
        # If no majority element is found
        return -1
