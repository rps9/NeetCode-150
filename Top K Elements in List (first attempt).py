class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}

        # Keeping a count of how many times you saw each number then sorting and taking the top k values
        for num in nums:
            try:
                nums_count[num] += 1
            except:
                nums_count[num] = 1

        sorted_nums_count = sorted(nums_count, key=lambda key: nums_count[key])
           
        return sorted_nums_count[-k:]

        
