class Solution:
    def trap(self, height: List[int]) -> int:
        # Go through and find all of the places water can be trapped
        # Water can be trapped when you go from high, to low, to high again
        i = 0
        peaks = []
        while i < len(height) - 1:
            change_in_y = height[i + 1] - height[i]
            if change_in_y < 0:
                peaks.append((height[i], i))
            if i == len(height) - 2 and change_in_y > 0: # Handles the last peak on the edge 
                peaks.append((height[i+1], i+1))
            i += 1

        i = 0
        peak_pairs = []
        while i < len(peaks) - 1:
            start_peak = peaks[i]
            current_max = (0, 0)
            for j in range(i+1, len(peaks)):
                if peaks[j][0] >= start_peak[0]:
                    end_peak = peaks[j]
                    i = j
                    break
                if current_max[0] < peaks[j][0]:
                    current_max = peaks[j]
                    end_peak_index = j
                if j == len(peaks) - 1:
                    end_peak = current_max
                    i = end_peak_index
            peak_pairs.append([start_peak, end_peak])

        water_count = 0
        for peak_pair in peak_pairs:
            start_point = peak_pair[0][1] + 1
            end_point = peak_pair[1][1]
            water_height = min(peak_pair[0][0], peak_pair[1][0])
            for i in range(start_point, end_point): 
                water_count += water_height - height[i]
            

        return water_count
