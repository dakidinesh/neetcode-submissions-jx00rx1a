class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        res=[]
        freq=[[] for i in range(len(nums)+1)]
        for i in nums:
            count[i]=1+count.get(i,0)
        
        for v,c in count.items():
            freq[c].append(v)
        
        for i in range(len(nums),-1,-1):
            for j in freq[i]:
                res.append(j)
                k-=1
                if k==0:
                    return res