'''
Power Set in Lexicographic order.
Examples : 
Input : abc
Output : a ab abc ac b bc c
The idea is to sort array first. 
After sorting, one by one fix characters and recursively generates all subsets starting from them. 
After every recursive call, we remove last character so that next permutation can be generated. 
'''
# Python3 program to generate power
# set in lexicographic order.

# str : Stores input string
# n : Length of str.
# curr : Stores current permutation
# index : Index in current permutation, curr
def permuteRec(string, n, index = -1, curr = ""):

    # base case
    if index == n:
        return

    if len(curr) > 0:
        print(curr)

    for i in range(index + 1, n):
        curr += string[i]
        permuteRec(string, n, i, curr)

        # backtracking
        curr = curr[:len(curr) - 1]

# Generates power set in lexicographic order
def powerSet(string):
    string = ''.join(sorted(string))
    permuteRec(string, len(string))

# Driver Code
if __name__ == "__main__":
    string = "cab"
    powerSet(string)

