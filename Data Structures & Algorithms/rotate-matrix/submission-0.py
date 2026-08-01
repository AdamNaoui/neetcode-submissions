class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N=len(matrix)
        l,r=0,N-1
        t,b=0,N-1

        while l<r and t<b:
            for i in range(r-l):
                temp=matrix[t][l+i]
                matrix[t][l+i]=matrix[b-i][l]
                matrix[b-i][l]=matrix[b][r-i]
                matrix[b][r-i]=matrix[t+i][r]
                matrix[t+i][r]=temp
            
            l+=1
            r-=1
            t+=1
            b-=1
        

        