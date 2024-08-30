class Solution:

    def encode(self, strs: List[str]) -> str:
        # Have each string start with the how many character it is then a special (non-number) character that tells the function when to stop reading the length
        single_string = ''
        for string in strs:
            single_string += f'{len(string)}*{string}'
        return single_string
    def decode(self, s: str) -> List[str]:
        # Initialize
        word_array = []
        i = 0
        
        # Use a while loop to better control where we are in the array
        while i < len(s):
            # Read the number string until it tells you to stop
            number_string = ''
            while s[i] != '*':
                number_string += s[i]
                i += 1
            string_length = int(number_string)
            i += 1 # Add one to get past the *
            word_array.append(s[i:i+string_length]) # Append the next length number of characters
            i += string_length # Move i to the beginning of the next length

        return word_array
