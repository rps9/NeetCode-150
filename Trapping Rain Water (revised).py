class Solution:
    def trap(self, height: List[int]) -> int:
        max_height_left = [0] * len(height)
        max_height_right = [0] * len(height)

        current_max_right = 0
        current_max_left = 0
        i = 0
        j = len(height) - 1

        # This can be accomplished in one pass with two pointers
        while i < len(height) - 1: # Do not include the last element because it cannot be a left/right max
            current_max_left = max(current_max_left, height[i])
            max_height_left[i + 1] = current_max_left
            current_max_right = max(current_max_right, height[j])
            max_height_right[j - 1] = current_max_right
            i += 1
            j -= 1
        
        # The amount of water that can be added at a point is the just the minimum of the two max heights that enclose it, minus the height blocking the water from the bottom
        total_water = 0
        for i in range(len(height)):
            added_water = min(max_height_left[i], max_height_right[i]) - height[i]
            if added_water > 0:
                total_water += added_water

        return total_water
