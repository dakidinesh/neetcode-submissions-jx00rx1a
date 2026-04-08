class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        countT,countS=[0]*26,[0]*26
        
        for i in range(len(s1)):
            countT[ord(s1[i])-ord('a')]+=1
            countS[ord(s2[i])-ord('a')]+=1

        if countT==countS: return True

        for i in range(len(s1),len(s2)):
            countS[ord(s2[i])-ord('a')]+=1
            countS[ord(s2[i-len(s1)])-ord('a')]-=1
            if countT==countS: return True
        return False

            

        



        

        