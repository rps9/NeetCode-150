from typing import List
from test_runner import test

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days_until_higher = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            print(stack)
            while stack:
                top_temp, top_index = stack[-1]
                if top_temp >= temp:
                    break
                stack.pop()
                days = i - top_index
                days_until_higher[top_index] = days
            stack.append((temp, i))
        
        return days_until_higher


def main():

    test_cases = [
        {"args": ([30,38,30,36,35,40,28],), "expected_result": [1,4,1,2,1,0,0]},
        {"args": ([22,21,20],), "expected_result": [0,0,0]},
        {"args": ([89,62,70,58,47,47,46,76,100,70],), "expected_result": [8,1,5,4,3,2,1,1,0,0]}
    ]

    test(Solution().dailyTemperatures, test_cases)

if __name__ == "__main__":
    main()