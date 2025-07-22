class Solution:

    def setUp(self, s1: str, s2: str) -> bool:
        # set the variables needed
        self.s1_len = len(s1)
        self.s2_len = len(s2)

        # check edge case
        self.edgeCase = False
        if self.s1_len > self.s2_len:
            self.edgeCase = True
            return 
        
        self.left_ptr = 0
        self.right_ptr = self.s1_len - 1

        self.matches_needed = 0
        self.matches_found = 0

        # create dictionary to keep track of matching letters
        self.s1_dict = {}
        for letter in s1:
            letter_freq = self.s1_dict.get(letter, 0)
            if letter_freq == 0:
                self.matches_needed += 1

            self.s1_dict[letter] =  letter_freq + 1

        # initialize the sliding window
        for i in range(self.s1_len):
            if s2[i] in self.s1_dict:
                self.s1_dict[s2[i]] -= 1

                if self.s1_dict[s2[i]] == 0:
                    self.matches_found += 1
                elif self.s1_dict[s2[i]] == -1:
                    self.matches_found -= 1
        
        return False

    def slideWindow(self, s2):
        # Function to quickly slide the window and update necassary values
        # This function assumes that you have checked boundaries beforehand
        remove_letter = s2[self.left_ptr]
        add_letter = s2[self.right_ptr + 1]

        self.left_ptr += 1
        self.right_ptr += 1

        if remove_letter in self.s1_dict:
            self.s1_dict[remove_letter] += 1

            if self.s1_dict[remove_letter] == 0:
                self.matches_found += 1
            elif self.s1_dict[remove_letter] == 1:
                self.matches_found -= 1

        if add_letter in self.s1_dict:
            self.s1_dict[add_letter] -= 1

            if self.s1_dict[add_letter] == 0:
                self.matches_found += 1
            elif self.s1_dict[add_letter] == -1:
                self.matches_found -= 1



    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        self.setUp(s1, s2)
        
        if self.edgeCase:
            return False
        
        while self.matches_found != self.matches_needed and self.right_ptr != self.s2_len - 1:
            self.slideWindow(s2)
        
        return self.matches_found == self.matches_needed


def main():
    s1 = "abc"
    s2 = "lecabee"
    print(Solution().checkInclusion(s1, s2))

if __name__ == "__main__":
    main()