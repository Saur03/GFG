'''
An Interesting Method to Generate Binary Numbers from 1 to n.
Given a number N, write a function that generates and prints all binary numbers with decimal values from 1 to N. 

Examples: 

Input: n = 2
Output: 1, 10

Input: n = 5
Output: 1, 10, 11, 100, 101
'''
# Function to generate binary numbers from 1 to n
def generatePrintBinary(n):
    for i in range(1, n + 1):
        str = ""
        temp = i
        # Convert decimal number to binary number
        while temp:
            if temp & 1:
                str = "1" + str
            else:
                str = "0" + str
            temp >>= 1  # Right shift the bits of temp by 1 position
        print(str)


n = 10

# Function call
generatePrintBinary(n)
