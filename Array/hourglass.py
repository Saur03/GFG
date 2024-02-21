'''
Given a 6X6 2D Array, arr:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

An hourglass in A is a subset of values with indices falling in this pattern in Arr's graphical representation:

a b c
  d
e f g
There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, 
then print the maximum hourglass sum. The array will always be 6X6.
Example
arr=
-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
The 16 hourglass sums are:

-63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18
The highest hourglass sum is 28 from the hourglass beginning at row 1, column 2:

0 4 3
  1
8 6 6

i-1,j-1  i-1,j    i-1,j+1
          ij
i+1,j-1  i+1,j    i+1,j+1

11, 12, 13, 14
21, 22, 23, 24
31, 32, 33, 34
41, 42, 43, 44
'''
def hourglassSum(arr):
    max=-float('inf')
    for i in range(1,5):
        for j in range(1,5):
            sum=0
            sum+=arr[i][j]
            sum+=arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]
            sum+=arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]

            if sum>max:
                max=sum
    return max     

'''
TC: O(n^2)
SC: O(1)
'''