class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Go through the array and make sure the queue always have unique values, when you come across a value that is in the set
        # remove characters until you remove that one
        current_chars = set()
        chars_queue = []
        longest_length = 0

        for char in s:
            if char in current_chars:
                longest_length = max(longest_length, len(current_chars))
                while chars_queue[0] != char:
                    current_chars.remove(chars_queue[0])
                    chars_queue.pop(0)
                current_chars.remove(chars_queue[0])
                chars_queue.pop(0)                
            current_chars.add(char)
            chars_queue.append(char)
        longest_length = max(longest_length, len(current_chars))
        return longest_length
        
