'''
Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).
Note: The drive code prints "balanced" if function return true, otherwise it prints "not balanced".

Example 1:
Input:{([])}
Output: true
Explanation: 
{ ( [ ] ) }. Same colored brackets can form balanced pairs, with 0 number of unbalanced bracket.

Example 2:
Input: ()
Output: true
Explanation: (). Same bracket can form balanced pairs, and here only 1 type of bracket is present and in balanced way.

Example 3:
Input: ([]
Output: false
Explanation: ([]. Here square bracket is balanced but the small bracket is not balanced and Hence , the output will be unbalanced.
'''
class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        stack = []
        # Dictionary to store the mapping of opening and closing brackets.
        bracket_mapping = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the expression.
        for char in x:
            # If the current character is a closing bracket.
            if char in bracket_mapping:
                # Pop the top element from the stack if it's not empty,
                # otherwise assign a dummy value to help with comparison.
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the corresponding opening bracket.
                if bracket_mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack.
                stack.append(char)
        
        # If the stack is empty, the brackets are balanced.
        return not stack

