class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        ans = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    product *= nums[j]
            ans[i] = product
            product = 1
        return ans
