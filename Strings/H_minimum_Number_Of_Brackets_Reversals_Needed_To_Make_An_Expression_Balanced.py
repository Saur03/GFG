'''
Minimum number of bracket reversals needed to make an expression balanced.
Given an expression with only ‘}’ and ‘{‘. 
The expression may not be balanced. 
Find minimum number of bracket reversals to make the expression balanced.
Examples: 

Input:  exp = "}{"
Output: 2
We need to change '}' to '{' and '{' to
'}' so that the expression becomes balanced, 
the balanced expression is '{}'
Input:  exp = "{{{"
Output: Can't be made balanced using reversals
Input:  exp = "{{{{"
Output: 2 
Input:  exp = "{{{{}}"
Output: 1 
Input:  exp = "}{{}}{{{"
Output: 3
'''
# Python program to find minimum number of
# reversals required to balance an expression

# Returns count of minimum reversals for making
# expr balanced. Returns -1 if expr cannot be
# balanced.
def countMinReversals(s):
    temp, res, n = 0, 0, len(s)

    if (n % 2 != 0):
        return -1
    for i in range(n):
        if (s[i] == '{'):
            temp += 1
        else:
            if (temp == 0):
                res += 1
                temp += 1
            else:
                temp -= 1

    if (temp > 0):
        res += temp // 2
    return res

# Driver program to test above function
expr = "}}{{"
print(countMinReversals(expr))

