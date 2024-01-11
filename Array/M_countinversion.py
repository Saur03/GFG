'''
Given an array of integers. Find the Inversion Count in the array. 
Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. 
If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Example 1:
Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

Example 2:
Input: N = 5
arr[] = {2, 3, 4, 5, 6}
Output: 0
Explanation: As the sequence is already sorted so there is no inversion count.

Example 3:
Input: N = 3, arr[] = {10, 10, 10}
Output: 0
Explanation: As all the elements of array are same, so there is no inversion count.
'''
class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Function to merge two sorted arrays and count inversions
        def merge(arr, temp, left, mid, right):
            i = left  # Index for the left subarray
            j = mid + 1  # Index for the right subarray
            k = left  # Index for the merged array
            inv_count = 0  # Initialize inversion count

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    k += 1
                    i += 1
                else:
                    # If arr[i] > arr[j], there are inversions with all the remaining elements in the left subarray
                    temp[k] = arr[j]
                    k += 1
                    j += 1
                    inv_count += (mid - i + 1)

            # Copy the remaining elements of left subarray (if any)
            while i <= mid:
                temp[k] = arr[i]
                k += 1
                i += 1

            # Copy the remaining elements of right subarray (if any)
            while j <= right:
                temp[k] = arr[j]
                k += 1
                j += 1

            # Copy back the merged elements to the original array
            for i in range(left, right + 1):
                arr[i] = temp[i]

            return inv_count

        # Function to perform merge sort and count inversions
        def merge_sort(arr, temp, left, right):
            inv_count = 0  # Initialize inversion count

            if left < right:
                mid = (left + right) // 2

                # Recursively count inversions in the left and right subarrays
                inv_count += merge_sort(arr, temp, left, mid)
                inv_count += merge_sort(arr, temp, mid + 1, right)

                # Merge the two sorted subarrays and count inversions
                inv_count += merge(arr, temp, left, mid, right)

            return inv_count

        # Create a temporary array for merge sort
        temp = [0] * n

        # Call the merge_sort function to count inversions
        result = merge_sort(arr, temp, 0, n - 1)

        return result
