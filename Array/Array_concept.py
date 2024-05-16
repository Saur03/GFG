'''
Functions in this library
-> Append
    |_ Takes value as an argument
    |_ Adds value at the end of the array
    |_ O(n)/O(1)
-> Insert
    |_ Takes index and value as arguments
    |_ Adds value at the given index
    |_ O(n)
-> Pop
    |_ Takes index as an argument
    |_ Removes value from the given index
-> Remove
    |_ Takes value as an argument
    |_ Removes the value if found
-> Index
    |_ Takes value as an argument
    |_ Provides the index of the element in the array
-> Reverse 
    |_ No argument
    |_ Reverses the array
 '''

import array

def printArray(arr):
    print ("Array: ",end="")
    for i in range (0,len(arr)):
        print (arr[i], end=" ")
    print("\n")

if __name__ == "__main__":
    # Initialize an array
    arr= array.array('i',[1, 2, 3, 1, 5])
    printArray(arr)

    # Try various functions
    arr.append(10)
    printArray(arr)

    arr.insert(3, 20)
    printArray(arr)

    arr.pop(-1)
    printArray(arr)

    arr.remove(20)
    printArray(arr)

    idx = arr.index(3)
    print ("Index of 3 is ", idx, "\n")

    arr.reverse()
    printArray(arr)

    # Extra functions
    print (arr.typecode)
    print (arr.itemsize)
    print (arr.buffer_info)
    print (arr.count(1))

    arr1 = array.array('i', [10,20,30])
    arr.extend(arr1)
    printArray(arr)

    li = [100, 200, 300]
    arr.fromlist(li)
    printArray(arr)

    new_list = arr.tolist()
    printArray(new_list)


