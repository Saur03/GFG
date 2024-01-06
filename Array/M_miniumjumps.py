'''
Given an array of N integers arr[] where each element represents the maximum length of the jump that can be made forward from that element. 
This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
Find the minimum number of jumps to reach the end of the array (starting from the first element). 
If an element is 0, then you cannot move through that element.

Note: Return -1 if you can't reach the end of the array.
'''
class Solution:
    def minJumps(self, arr, n):
        if n <= 1:
            return 0

        if arr[0] == 0:
            return -1

        max_reach = arr[0]  # Represents the farthest index that can be reached from the current position
        steps = arr[0]  # Represents the number of steps that can be taken from the current position
        jumps = 1  # Represents the minimum number of jumps required to reach the end

        for i in range(1, n):
            if i == n - 1:
                return jumps

            max_reach = max(max_reach, i + arr[i])
            steps -= 1

            if steps == 0:
                jumps += 1

                if i >= max_reach:
                    return -1

                steps = max_reach - i

        return -1

# Example usage:
solution_obj = Solution()

arr1 = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n1 = len(arr1)
print(solution_obj.minJumps(arr1, n1))  # Output: 3

arr2 = [1, 4, 3, 2, 6, 7]
n2 = len(arr2)
print(solution_obj.minJumps(arr2, n2))  # Output: 2
