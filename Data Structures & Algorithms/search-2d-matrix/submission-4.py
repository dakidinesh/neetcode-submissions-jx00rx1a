class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])
        l,r=0,len(matrix[0])
        top,bottom=0,len(matrix)-1
        while top<=bottom:
            m=(top+bottom)//2
            if target<matrix[m][0]:
                bottom=m-1
            elif target>matrix[m][-1]:
                top=m+1
            else:
                break
        l,r=0,len(matrix[0])-1
        m=(top+bottom)//2
        while l<=r:
            n=(l+r)//2
            if target>matrix[m][n]:
                l=n+1
            elif target<matrix[m][n]:
                r=n-1
            else:
                return True
        return False
