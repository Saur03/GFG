'''
Python | Sum of number digits in List
Output : 
The original list is : [12, 67, 98, 34]
List Integer Summation : [3, 13, 17, 7]

Using map() function and modulo operator :

Step-by-step algorithm for implementing the approach

1) First, define a function digit_sum(num) which takes a single number as input and returns the sum of its digits

Initialize a variable digit_sum to 0.
Apply a while loop to extract the last digit of the number using the modulo operator (%) and add it to the digit_sum variable.
Divide the number by 10 using floor division operators (//) to remove the last digit.
Repeat sub point 2 and 3 until the number becomes zero.
Return the digit_sum variable.
2) Define a function sum_of_digits_list(lst) which will takes a list of numbers as input and returns a list containing the sum of digits of each number in the input list, using the following steps:

Apply map() function to the digit_sum() function.
Convert the resulting map object to a list using the list() function.
Return the resulting list.
3) Define a list of numbers lst which will calculate the sum of digits.

4) Now wecall the sum_of_digits_list(lst) function with lst as the input.

5) Print the resulting list.
'''
lst = [12, 67, 98, 34]
def digit_sum(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum
 
def sum_of_digits_list(lst):
    return list(map(digit_sum, lst))
 
print(sum_of_digits_list(lst))