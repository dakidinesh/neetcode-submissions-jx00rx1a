class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        d={')':'(', '}':'{',']':'['}
        for i in s:
            if i in d:
                if d[i]==a.pop():
                    continue
                else:
                    return False
            a.append(i)
        if len(a)==0:
            return True
        
                
            

        