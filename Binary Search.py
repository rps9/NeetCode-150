from typing import List
from test_runner import test

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1
        while left_index <= right_index:
            guess_index = int((right_index + left_index) / 2)
            guess = nums[guess_index]
            
            if guess == target:
                return guess_index
            elif guess < target:
                left_index = guess_index + 1
            else:
                right_index = guess_index - 1
        
        return -1
    
def main():
    test_cases = [
        {"args": ([-1,0,2,4,6,8], 4), "expected_result": 3},
        {"args": ([-1,0,2,4,6,8], 3), "expected_result": -1}
    ]

    test(Solution().search, test_cases)

if __name__ == "__main__":
    main()