class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]

        def backtracking(openS,closeS):
            if openS==closeS==n:
                res.append("".join(stack))
                return
            if openS<n:
                stack.append("(")
                backtracking(openS+1,closeS)
                stack.pop()
            if closeS<openS:
                stack.append(")")
                backtracking(openS,closeS+1)
                stack.pop()
        
        backtracking(0,0)
        return res
            
        