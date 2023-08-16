'''
Program to count occurrence of a given character in a string
Input : str = "geeksforgeeks"
         c = 'e'
Output : 4
'e' appears four times in str.

Input : str = "abccdefgaa"
          c = 'a' 
Output : 3
'a' appears three times in str.
'''
def count(s, c) :
    # Count variable
    res = 0
    for i in range(len(s)) :
        # Checking character in string
        if (s[i] == c):
            res = res + 1
    return res    

str= "geeksforgeeks"
c = 'e'
print(count(str, c))
