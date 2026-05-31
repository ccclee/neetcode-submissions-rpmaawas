class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length = len(matrix)
        for i in range(0, length):
            for j in range(i+1, length):
                matrix[i][j], matrix[j][i] =   matrix[j][i], matrix[i][j]
        
        for i in range(length):
            for j in range(length//2):
                matrix[i][j], matrix[i][length-1-j] =   matrix[i][length-1-j], matrix[i][j]
        

        

        