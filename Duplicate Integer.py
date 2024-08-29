class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Time: O(n)
        # Space: O(n)
        
        # Create a dictionary for the numbers seen
        seen_nums = {}

        # Loop through the array
        for num in nums:
            try:
                seen_nums[num]
                return True
            except:
                seen_nums[num] = True
        
        return False
            
