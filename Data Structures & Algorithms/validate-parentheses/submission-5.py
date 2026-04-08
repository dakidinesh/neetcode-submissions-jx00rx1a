class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen={')':'(','}':'{',']':'['}
        stack=[]
        for i in s:
            if stack and i in closeToOpen and stack[-1]==closeToOpen[i]:
                stack.pop()
            else:
                stack.append(i)
        return True if not stack else False
