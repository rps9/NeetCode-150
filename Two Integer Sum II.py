class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Use two pointer approach to find the solution
        i = 0
        j = len(numbers) - 1 
        while i < j: 
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1, j+1] # We can assume that the solution always exists
