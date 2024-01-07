'''
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.
'''
# we have use the Dutch National Flag algorithm to sort an array containing only 0s, 1s, and 2s in ascending order. This algorithm was designed by Edsger W. Dijkstra and is efficient for this specific scenario.
class Solution:
    def sort012(self,arr,n):
        # code here
        low, mid, high = 0, 0, len(arr) - 1
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr