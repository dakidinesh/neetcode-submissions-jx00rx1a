class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a=[0]*len(temperatures)
        stack=[]

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                a[stackIndex]=i-stackIndex
            stack.append((t,i))
        return a