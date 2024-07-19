'''
Count number of equal pairs in a string
Given a string s, find the number of pairs of characters that are same. 
Pairs (s[i], s[j]), (s[j], s[i]), (s[i], s[i]), (s[j], s[j]) should be considered different. 

Examples :

Input: air
Output: 3
Explanation :
3 pairs that are equal are (a, a), (i, i) and (r, r)
Input : geeksforgeeks
Output : 31
'''
# Function to count the number of equal pairs
def countPairs(s):
    # Length of the string
    n = len(s)

    # Initialize the answer
    ans = 0

    # Running nested loops to check equal pairs
    for i in range(n):
        for j in range(n):
            # When such pair is found
            if s[i] == s[j]:
                ans += 1

    return ans

# Driver Code
if __name__ == "__main__":
    s = "geeksforgeeks"
    print(countPairs(s))
