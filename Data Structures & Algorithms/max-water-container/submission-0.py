class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        MaxWater=0
        while l<r:
            MaxWater = max((r-l)*min(heights[l],heights[r]), MaxWater)
            if heights[l]<heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
            else:
                l+=1
            
        return MaxWater
            
        
        
        