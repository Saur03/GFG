'''
Decode a string recursively encoded as count followed by substring.
An encoded string (s) is given, the task is to decode it. The pattern in which the strings are encoded is as follows. 

<count>[sub_str] ==> The substring 'sub_str' 
                      appears count times.

Examples:  

Input : str[] = "1[b]"
Output : b
Input : str[] = "2[ab]"
Output : abab
Input : str[] = "2[a2[b]]"
Output : abbabb
Input : str[] = "3[b2[ca]]"
Output : bcacabcacabcaca
'''
# Python program to decode a string recursively 
# encoded as count followed substring 

# Returns decoded string for 'str' 
def decode(Str):
    integerstack = []
    stringstack = []
    temp = ""
    result = "" 
    i = 0
    # Traversing the string 
    while i < len(Str):
        count = 0

        # If number, convert it into number 
        # and push it into integerstack. 
        if (Str[i] >= '0' and Str[i] <='9'):
            while (Str[i] >= '0' and Str[i] <= '9'):
                count = count * 10 + ord(Str[i]) - ord('0') 
                i += 1
            i -= 1
            integerstack.append(count)

        # If closing bracket ']', pop element until 
        # '[' opening bracket is not found in the 
        # character stack. 
        elif (Str[i] == ']'):
            temp = "" 
            count = 0

            if (len(integerstack) != 0):
                count = integerstack[-1] 
                integerstack.pop()

            while (len(stringstack) != 0 and stringstack[-1] !='[' ):
                temp = stringstack[-1] + temp 
                stringstack.pop()

            if (len(stringstack) != 0 and stringstack[-1] == '['): 
                stringstack.pop() 

            # Repeating the popped string 'temo' count 
            # number of times.
            for j in range(count):
                result = result + temp 

            # Push it in the character stack.
            for j in range(len(result)):
                stringstack.append(result[j]) 

            result = ""

        # If '[' opening bracket, push it into character stack. 
        elif (Str[i] == '['):
            if (Str[i-1] >= '0' and Str[i-1] <= '9'): 
                stringstack.append(Str[i]) 

            else:
                stringstack.append(Str[i]) 
                integerstack.append(1)

        else:
            stringstack.append(Str[i])
        
        i += 1

    # Pop all the element, make a string and return.
    while len(stringstack) != 0:
        result = stringstack[-1] + result 
        stringstack.pop()

    return result

# Driven code 
if __name__ == '__main__':
    Str = "3[b2[ca]]"
    print(decode(Str))
    
