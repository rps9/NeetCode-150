class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time: O(nlogn)
        # Space: O(n)

        # Two pointer approach was my first intuition here, a hashmap is better 
        sorted_nums = nums.copy()
        sorted_nums.sort()

        left_ptr = 0
        right_ptr = len(nums) - 1

        while left_ptr != right_ptr:
            if sorted_nums[left_ptr] + sorted_nums[right_ptr] <  target:
                left_ptr += 1
            elif sorted_nums[left_ptr] + sorted_nums[right_ptr] >  target:  
                right_ptr -= 1
            else:
                break

        i = 0
        left_index = -1
        right_index = -1

        while left_index == -1 or right_index == -1: 
            print(nums[i])
            
            if (nums[i] == sorted_nums[left_ptr] or nums[i] == sorted_nums[right_ptr]) and left_index == -1:
                left_index = i
            elif (nums[i] == sorted_nums[left_ptr] or nums[i] == sorted_nums[right_ptr]):
                right_index = i
            i += 1

        return [left_index, right_index]
