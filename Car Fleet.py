from typing import List
from test_runner import test

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = list(zip(position, speed))
        position_speed.sort(reverse=True, key=lambda x: x[0])
        time_bottleneck = -1
        groups = 0

        for i in range(len(position)):
            i_position = position_speed[i][0]
            i_speed = position_speed[i][1]

            time = (target - i_position) / i_speed

            if time > time_bottleneck:
                groups += 1
                time_bottleneck = time

            
        return groups
        
def main():
    test_cases = [
        {"args": (10, [4,1,0,7], [2,2,1,1]), "expected_result": 3},
        {"args": (10, [1,4], [3,2]), "expected_result": 1},
        {"args": (10, [0,4,2], [2,1,3]), "expected_result": 1},
        {"args": (10, [8,3,7,4,6,5], [4,4,4,4,4,4]), "expected_result": 6}
    ]

    test(Solution().carFleet, test_cases)

if __name__ == "__main__":
    main()