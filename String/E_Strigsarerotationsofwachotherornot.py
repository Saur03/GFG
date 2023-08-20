'''
Check if given strings are rotations of each other or not
Input: S1 = ABCD, S2 = CDAB
Output: Strings are rotations of each other

Input: S1 = ABCD, S2 = ACBD
Output: Strings are not rotations of each other
'''
def are_rotations(str1, str2):
    # Check if lengths of both strings are the same
    if len(str1) != len(str2):
        return False
    concatenated = str1 + str1  # Concatenate str1 with itself
    if str2 in concatenated:
        return True
    else:
        return False
    
string1 = "abcde"
string2 = "cdeab"
if are_rotations(string1, string2):
    print("Strings are rotations of each other.")
else:
    print("Strings are not rotations of each other.")        