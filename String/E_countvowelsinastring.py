'''
Program to count vowels in a string (Iterative and Recursive)
Input : abc de
Output : 2

Input : geeksforgeeks portal
Output : 7
'''
def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']

def countVowels(str):
    count = 0
    for i in range(len(str)):
        if isVowel(str[i]):
            count += 1
    return count

str = 'abc de'
print(countVowels(str))        
                