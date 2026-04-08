class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq=[[] for i in range(len(nums)+1)]
        a=[]

        for i in nums:
            count[i] = 1 + count.get(i,0)
        
        for i,c in count.items():
            freq[c].append(i)
        
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                a.append(j)
                if len(a)==k:
                    return a 