class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        boool = False
        for i in range(len(nums)):
            if nums.count(nums[i]) > 1:
                boool = True
        return boool