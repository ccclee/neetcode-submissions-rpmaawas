class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        def outercircle(s,w,l):
            nonlocal res
            if w<0 or l <0:
                return res
            if w ==0 and l==0:
                res.append(matrix[s][s])
                return res
            if w ==0:
                for i in range(l+1):
                    res.append(matrix[s+i][s])
                return res
            if l ==0:
                for i in range(w+1):
                    res.append(matrix[s][s+i])
                return res
            for j in range(s,s+w):
                res.append(matrix[s][j])
            for i in range(s,s+l):
                res.append(matrix[i][s+w])
            for j in range(s+w,s,-1):
                res.append(matrix[s+l][j])
            for i in range(s+l,s,-1):
                res.append(matrix[i][s])
            return outercircle(s+1,w-2,l-2)

        return outercircle(0,len(matrix[0])-1,len(matrix)-1)

        