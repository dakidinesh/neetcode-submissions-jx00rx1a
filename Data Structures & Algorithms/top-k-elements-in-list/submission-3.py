class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        count=[[]for i in range(len(nums)+1)]
        for i in nums:
            freq[i]=1+freq.get(i,0)
        
        for v,c in freq.items():
            count[c].append(v)
        res=[]
        for i in range(len(nums),-1,-1):
            for j in count[i]:
                res.append(j)
                k-=1
                if k==0:
                    return res