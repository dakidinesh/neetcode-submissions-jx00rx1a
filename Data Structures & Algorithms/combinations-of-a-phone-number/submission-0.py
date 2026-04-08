class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        digitTochar = {
                        "2":"abc",
                        "3":"def",
                        "4":"ghi",
                        "5":"jkl",
                        "6":"mno",
                        "7":"pqrs",
                        "8":"tuv",
                        "9":"wxyz"
                      }
        
        def backtracking(i,cur):
            if len(cur)==len(digits):
                res.append(cur)
                return
            for j in digitTochar[digits[i]]:
                backtracking(i+1,cur+j)
        if digits:
            backtracking(0,"")
        return res