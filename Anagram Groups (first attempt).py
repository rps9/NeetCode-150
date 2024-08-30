class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Sorts each word and groups it based off of the sorting, not the ideal solution
        word_counts = {}
        grouped_words = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            try:
                word_counts[sorted_word].append(word)
            except:
                word_counts[sorted_word] = [word]
        
        for group in word_counts:
            grouped_words.append(word_counts[group])
            
    
        return grouped_words

        
