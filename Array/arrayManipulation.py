'''
Starting with a 1-indexed array of zeros and a list of operations, 
for each operation add a value to each the array element between two given indices, inclusive. 
Once all operations have been performed, return the maximum value in the array.
Example:-
n = 10
queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]

Queries are interpreted as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1

Add the values of k between the indices a and b inclusive:

index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]
The largest value is 10 after all operations are performed.
'''
def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    for q in queries:
        start, end, amt = q
        arr[start-1]+=amt
        arr[end]-=amt
        
    mv=-1
    larv=0
    for a in arr:
        larv+=a
        if larv>mv:
            mv=larv
    return mv       
