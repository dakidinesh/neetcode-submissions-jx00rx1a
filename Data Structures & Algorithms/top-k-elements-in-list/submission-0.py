class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=[]
        for i in nums:
            if nums.count(i)>=k:
                a.append(i)
        return sorted(a)

            
        