class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        d={')':'(', '}':'{',']':'['}
        if len(s)%2!=0:
            return False

        for i in s:
            if i in d:
                if (len(a)!=0 and d[i]==a.pop()):
                    continue
                else:
                    return False
            a.append(i)
        if len(a)==0:
            return True
        else:
            return False
        
                
            

        