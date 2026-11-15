class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=[]
        res=0
        for i in tokens:
            if i.isdigit():
                a.append(int(i))
            elif i=='+':
                a.append(a.pop()+a.pop())
            elif i=='-':
                a.append(a.pop()-a.pop())
            elif i=='*':
                a.append(a.pop()*a.pop())
            elif i=='/':
                a.append(a.pop()/a.pop())
        return a[0]
            


        