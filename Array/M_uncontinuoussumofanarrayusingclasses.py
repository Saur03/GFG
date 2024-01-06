#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self, arr, n, s):
        result = []
        current_sum = 0
        start = 0

        for end in range(n):
            current_sum += arr[end]

            while current_sum > s and start <= end:
                current_sum -= arr[start]
                start += 1

            if current_sum == s:
                result.append(start + 1)  
                result.append(end + 1)    
                return result

        result.append(-1)
        return result


sol = Solution()

arr1 = [1, 2, 3, 7, 5]
n1, s1 = 5, 12
output1 = sol.subArraySum(arr1, n1, s1)
print(f'{output1[0]} {output1[1]}') 