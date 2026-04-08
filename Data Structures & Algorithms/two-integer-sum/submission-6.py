class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stack={}
        for i,v in enumerate(nums):
            if (target-v) in stack:
                return [stack[target-v],i]
            stack[v]=i