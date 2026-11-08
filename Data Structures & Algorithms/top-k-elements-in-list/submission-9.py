class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        res=[]
        freq=[[] for i in range(len(nums)+1)]

        for i in range(len(nums)):
            count[nums[i]]=1+count.get(nums[i],0)

        for val,cnt in count.items():
            freq[cnt].append(val)
        
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res