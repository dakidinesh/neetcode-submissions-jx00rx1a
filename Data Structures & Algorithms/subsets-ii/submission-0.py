class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        def backtracking(i,subset):
            if i==len(nums):
                res.append(subset[::])
                return
            
            #inclues nums[i]
            subset.append(nums[i])
            backtracking(i+1,subset)
            subset.pop()

            #doesn't include nums[i]
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            backtracking(i+1,subset)
        backtracking(0,[])
        return res