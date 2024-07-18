'''
Divide large number represented as string.
Given a large number (represented as a string) which has to divide by another number (represented as int data type). 
The large number can be very large which does not even fit in long long in C++. 
The task is to find the division of these numbers.

Examples: 

Input : number  = 1260257
        divisor = 37
Output : 34061
(See below diagram)
Input : number  = 12313413534672234
        divisor = 754
Output : 16330787181262
Input : number  = 1248163264128256512
        divisor = 125
Output : 9985306113026052
'''
# Python3 program to implement division with large number 
import math

# A function to perform division of large numbers 
def longDivision(number, divisor): 

    # As result can be very large store it in string 
    ans = ""; 
    
    # Find prefix of number that is larger than divisor. 
    idx = 0; 
    temp = ord(number[idx]) - ord('0');
    while (temp < divisor):
        temp = (temp * 10 + ord(number[idx + 1]) -
                            ord('0'));
        idx += 1;
    
    idx += 1;

    # Repeatedly divide divisor with temp. 
    # After every division, update temp to include one more digit. 
    while ((len(number)) > idx): 
        
        # Store result in answer i.e. temp / divisor 
        ans += chr(math.floor(temp // divisor) + ord('0')); 
        
        # Take next digit of number
        temp = ((temp % divisor) * 10 + ord(number[idx]) -
                                        ord('0'));
        idx += 1;

    ans += chr(math.floor(temp // divisor) + ord('0'));
    
    # If divisor is greater than number 
    if (len(ans) == 0): 
        return "0"; 
    
    # else return ans 
    return ans; 

# Driver Code
number = "1248163264128256512"; 
divisor = 125; 
print(longDivision(number, divisor)); 
    
