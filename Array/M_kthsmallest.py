'''
Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. 
It is given that all array elements are distinct.

Note :-  l and r denotes the starting and ending index of the array.

Example 1:
Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
L=0 R=5
Output : 7
Explanation :- 3rd smallest element in the given array is 7.

Example 2:
Input:
N = 5
arr[] = 7 10 4 20 15
K = 4 L=0 R=4
Output : 15
Explanation :- 4th smallest element in the given array is 15.
'''
# we can solve this problem using the quickselect algorithm, which is a variation of the quicksort algorithm. The idea is to partition the array and recursively process only the part of the array that contains the Kth smallest element.

class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        def quickselect(arr, low, high, k):
            if low <= high:
                pivot_index = partition(arr, low, high)

                if pivot_index == k:
                    return arr[pivot_index]
                elif pivot_index < k:
                    return quickselect(arr, pivot_index + 1, high, k)
                else:
                    return quickselect(arr, low, pivot_index - 1, k)

        return quickselect(arr, l, r, k - 1)
