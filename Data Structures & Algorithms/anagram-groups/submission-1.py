class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)

        for i in strs:
            count=[0]*26
            for c in i:
                count[ord(c)-ord('a')] += 1
            
            a[tuple(count)].append(i)
        return a.values()
        
                
        