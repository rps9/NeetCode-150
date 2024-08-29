class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        # Better approach using a hashmap
        nums_hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in nums_hashmap:
                return[nums_hashmap[target - nums[i]], i]
            else:
                nums_hashmap[nums[i]] = i
