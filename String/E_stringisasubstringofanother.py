'''
Check if a string is substring of another
example- Input: S1 = “for”, S2= “geeksforgeeks”
Output: 5
Explanation: String “for” is present as a substring of s2.

Input: S1 = “practice”, S2= “geeksforgeeks”
Output: -1.
Explanation: There is no occurrence of “practice” in “geeksforgeeks”
'''
def isSubstring(s1, s2):
    if s1 in s2:
        return s2.index(s1)
    return -1

if __name__ == "__main__":
    s1 = "for"
    s2 = "geeksforgeeks"
    res = isSubstring(s1, s2)
    if res == -1:
        print("Not present")
    else:
        print("Present at index " + str(res))    