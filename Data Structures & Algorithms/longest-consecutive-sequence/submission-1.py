class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest=0
        for i in nums:
            if i-1 not in nums:
                j=i
                long=0
                while j in nums:
                    long+=1
                    j+=1
                longest=max(longest,long)
        return longest