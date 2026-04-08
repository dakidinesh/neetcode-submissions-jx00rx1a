class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i,v in enumerate(nums):
            diff=target-v
            if diff in a:
                return [a[diff],i]
            a[v]=i