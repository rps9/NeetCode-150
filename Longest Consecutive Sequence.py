class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # The key making the list a set which is O(n) time
        nums = set(nums)

        longest_sequence = 0
        for num in nums:
            if num - 1 not in nums:
                # This is a start value
                sequence_length = 1
                i = 1
                # Build out the whole sequence
                while num + i in nums:
                    i += 1
                    sequence_length += 1
                if sequence_length > longest_sequence:
                    longest_sequence = sequence_length
        return longest_sequence
