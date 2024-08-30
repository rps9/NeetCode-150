class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Creates an array of the number of characters for each word and uses that to hash
        # Biggest piece is realizing you need to make the array a tuple when you are done so you can actually hash into the hashtable
        word_count = {}
        for word in strs:
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1 # Subtract a from the value of the current character to start at 0 index
            try:
                word_count[tuple(char_count)].append(word)
            except:
                word_count[tuple(char_count)] = [word]
        

        return word_count.values()

        
