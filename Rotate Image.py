from typing import List
from test_runner import test

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Rotate 90 degrees clockwise is just transpose then reverse
        n = len(matrix)

        # transpose in place
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row in place
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1



def main():
    test_cases = [
        {"args": ([[1, 2], [3, 4]],), "expected_result": [[3, 1], [4, 2]]},
        {"args": ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), "expected_result": [[7, 4, 1], [8, 5, 2], [9, 6, 3]]},
    ]

    def run(matrix):
        Solution().rotate(matrix)
        return matrix

    test(run, test_cases)

if __name__ == "__main__":
    main()
