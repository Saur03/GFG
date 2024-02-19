'''
Declare a 2-dimensional array, arr, of n empty arrays. All arrays are zero indexed.
Declare an integer, lastAnswer, and initialize it to 0.

There are 2 types of queries, given as an array of strings for you to parse:

Query: 1 x y
Let idx = ((x^lastAnswer) % n).
Append the integer y to  arr[idx].
Query: 2 x y
Let idx = ((x^lastAnswer) % n).
Assign the value arr[idx][y % len(arr[idx])] to lastAnswer.
Store the new value of lastAnwer to an answers array.
Function Description

Complete the dynamicArray function below.

dynamicArray has the following parameters:
- int n: the number of empty arrays to initialize in 
- string queries[q]: query strings that contain 3 space-separated integers

Returns

int[]: the results of each type 2 query in the order they are presented
'''
def dynamicArray(n, queries):
    arr = [[] for i in range(0, n)]
    lastAnswer = 0
    ans = []
    
    for query in queries:
        type, x, y = query
        # query 1
        if type == 1:
            idx = ((x^lastAnswer) % n)
            arr[idx].append(y)
        # query 2
        elif type == 2:
            idx = ((x^lastAnswer) % n)
            lastAnswer = arr[idx][y % len(arr[idx])]
            ans.append(lastAnswer)
            
    return ans