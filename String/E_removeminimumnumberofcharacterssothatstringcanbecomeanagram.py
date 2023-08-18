'''
Remove minimum number of characters so that two strings become anagram
Examples :  

Input : str1 = "bcadeh" str2 = "hea"
Output: 3
We need to remove b, c and d from str1.

Input : str1 = "cddgk" str2 = "gcd"
Output: 2

Input : str1 = "bca" str2 = "acb"
Output: 0
'''
def makeAnagram(a, b):
    buffer = [0] * 26
    for char in a:
        buffer[ord(char) - ord('a')] += 1
    for char in b:
        buffer[ord(char) - ord('a')] -= 1
    return sum(map(abs, buffer))

if __name__ == "__main__" :
    str1 = "bcadeh"
    str2 = "hea"
    print(makeAnagram(str1, str2))        