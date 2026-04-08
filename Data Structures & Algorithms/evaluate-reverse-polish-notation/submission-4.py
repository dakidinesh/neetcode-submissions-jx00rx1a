class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=[]

        for i in tokens:
            if i=="+":
                a.append(a.pop()+a.pop())
            elif i=="-":
                b,c=a.pop(), a.pop()
                a.append(c-b)
            elif i=="*":    
                a.append(a.pop()*a.pop())
            elif i=="/":
                b,c=a.pop(), a.pop()
                a.append(int(c/b))
            else:
                a.append(int(i))
        return a[0]