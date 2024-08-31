class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if nums[i] == 0:
                if nums[i + 1] == 0 and nums[i + 2] == 0:
                    res.append([0, 0, 0])
                break
            if i == 0 or nums[i-1] != nums[i]:
                L = i + 1 # This was the problem, you should initialize L to i + 1 because you do not need to check the values behind it, that would result in duplicate arrays
                R = len(nums) - 1
                target_sum = -1 * nums[i]
                while L < R:
                    if L == i or target_sum > nums[L] + nums[R]:
                        L += 1
                    elif R == i or target_sum < nums[L] + nums[R]:
                        R -= 1
                    else:
                        res.append([nums[i], nums[L], nums[R]])
                        L += 1
                        while L < R and nums[L] == nums[L-1]:
                            L += 1
        return res
          
