from typing import List
from test_runner import test

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_size = len(matrix[0])

        for row in matrix:
            if target >= row[0] and target <= row[row_size]:
                print("do something")
                
def main():
    test_cases = [
        {"args": ([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10), "expected_result": True},
        {"args": ([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15), "expected_result": False},
    ]

    test(Solution().func, test_cases)

if __name__ == "__main__":
    main()