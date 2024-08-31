class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # The idea is to get the left and right products for each position and multiply them to get the product for that position
        
        left_products = [1]
        # Keep a running product, the first value being 1 and do not include the final value in nums because it is not in any left products
        for i in range(0, len(nums)-1):
            left_products.append(nums[i] * left_products[i])
        
        # Slightly different approach since you have to work in reverse, once again, do not include the leftmost value because it is in no right products
        right_products = [1] * len(nums)
        for i in range(len(nums) - 1, 0, -1):
            right_products[i - 1] = nums[i] * right_products[i]
        
        # Multiply the left and right products
        products = []
        for i in range(len(nums)):
            products.append(left_products[i] * right_products[i])
        return products 
