class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        hesh_table = {}
        for ind, name in enumerate(nums):
            hesh_table[name] = ind
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hesh_table and hesh_table[complement] != i:
                return sorted([i, hesh_table[complement]])