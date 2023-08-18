'''
Check whether two Strings are anagram of each other
Examples:
Input: str1 = “listen”  str2 = “silent”
Output: “Anagram”
Explanation: All characters of “listen” and “silent” are the same.
'''
def is_anagram(a, b):
    # Sort the strings
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    if sorted_a == sorted_b:
        return True
    else:
        return False
    
if __name__ == "__main__":
    a = "geeksforgeeks"
    b = "forgeeksgeeks"
    if is_anagram(a, b):
        print("YES, They are Anagram")
    else:
        print("NO, They are not Anagram")        
    

