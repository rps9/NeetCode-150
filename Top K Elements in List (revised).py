class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}
        count_array = []

        # Keep track of the number of times you saw each number 
        for num in nums:
            try:
                nums_count[num] += 1
            except:
                nums_count[num] = 1

        # Create the count array to be able to be inexed to up to the size of the array   
        for i in range(len(nums)+1):
            count_array.append([])
        
        for num in nums_count.items():
            count_array[num[1]].append(num[0]) # Add the number to the corresponding number of times it was seen

        # Get the top k elements 
        count = 0
        top_k_elements = []
        for i in range(len(count_array)-1, -1, -1):
            if count_array[i]:
                for number in count_array[i]:
                    count += 1
                    top_k_elements.append(number)
                    if count == k:
                        return top_k_elements

        
