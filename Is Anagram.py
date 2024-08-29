class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(s + t)
        # Space: O(s + t)

        # Create two dictionaries with the letter as the key and the number of times
        # it appears as the value then check if they are the same.
        word1_length = len(s)
        word2_length = len(t)

        if word1_length != word2_length:
            return False

        word1_dict = {}
        word2_dict = {}
        
        for i in range(word1_length):
            try:
                word1_dict[s[i]] += 1
            except:
                word1_dict[s[i]] = 1
            try:
                word2_dict[t[i]] += 1
            except:
                word2_dict[t[i]] = 1
            

        return word1_dict == word2_dict
        
