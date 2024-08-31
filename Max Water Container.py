class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Use two pointer approach to make the most ideal choices and find the max amount of water
        i = 0
        j = len(heights) - 1
        max_water = 0

        while i < j:
            current_water = min(heights[i], heights[j]) * (j - i) # Calculate area of water
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
            max_water = max(current_water, max_water) # Replace if it is greater than max_water

        return max_water

        
