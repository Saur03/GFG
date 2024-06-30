'''
K-th Largest Sum Contiguous Subarray

Given an array of integers. 
Write a program to find the K-th largest sum of contiguous subarray within the array of numbers 
that has both negative and positive numbers.

Examples: 
Input: a[] = {20, -5, -1}, K = 3
Output: 14
Explanation: All sum of contiguous subarrays are (20, 15, 14, -5, -6, -1) 
so the 3rd largest sum is 14.

Input: a[] = {10, -10, 20, -40}, k = 6
Output: -10
Explanation: The 6th largest sum among
sum of all contiguous subarrays is -10.
'''
# Python code to implement Prefix sum approach
import heapq

# The main function to find the K-th largest sum of
# contiguous subarray using Prefix Sum and Sorting
# approach.
def kthLargestSum(arr, k):
    n = len(arr)

    # Create a prefix sum array.
    prefixSum = [0] * (n + 1)
    for i in range(1, n+1):
        prefixSum[i] = prefixSum[i - 1] + arr[i - 1]

    # Create a heap to store K largest subarray sums.
    subarraySums = []
    heapq.heapify(subarraySums)
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            subarraySum = prefixSum[j] - prefixSum[i]
            if len(subarraySums) < k:
                heapq.heappush(subarraySums, subarraySum)
            else:
                if subarraySum > subarraySums[0]:
                    heapq.heapreplace(subarraySums, subarraySum)

    # Return the K-th largest sum of contiguous subarray.
    return subarraySums[0]

# Driver Code
if __name__ == '__main__':
    arr = [10, -10, 20, -40]
    k = 6
    print(kthLargestSum(arr, k)) # expected output is -10
