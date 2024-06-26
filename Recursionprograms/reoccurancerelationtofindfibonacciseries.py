'''
Write a program and recurrence relation to find the Fibonacci series of n where n>2 . 
Mathematical Equation:  

n if n == 0, n == 1;      
fib(n) = fib(n-1) + fib(n-2) otherwise;
Recurrence Relation: 

T(n) = T(n-1) + T(n-2) + O(1)
Recursive program: 

Input: n = 5 
Output:
Fibonacci series of 5 numbers is : 0 1 1 2 3
'''
# Python code to implement Fibonacci series 

# Function for fibonacci 
def fib(n): 

	# Stop condition 
	if (n == 0): 
		return 0

	# Stop condition 
	if (n == 1 or n == 2): 
		return 1

	# Recursion function 
	else: 
		return (fib(n - 1) + fib(n - 2)) 


# Driver Code 

# Initialize variable n. 
n = 5; 
print("Fibonacci series of 5 numbers is :",end=" ") 

# for loop to print the fibonacci series. 
for i in range(0,n): 
	print(fib(i),end=" ") 
