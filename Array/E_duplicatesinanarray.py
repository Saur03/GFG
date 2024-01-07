'''
Given an array a of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array. Return the answer in ascending order. If no such element is found, return list containing [-1]. 

Note: The extra space is only for the array to be returned. Try and perform all operations within the provided array. 
'''

class Solution:
    def duplicates(self, arr, n):
        res = set()
        for i in range(n):
            arr[i] += 1
        for i in arr:
            if arr[abs(i)-1]<0:
                res.add(abs(i)-1)
            else:
                arr[abs(i)-1] *= -1
        if len(res) == 0:
            return [-1]
        return sorted(res)                