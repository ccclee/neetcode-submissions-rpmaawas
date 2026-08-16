class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def help(left,right,curr):
            if left == 0 and right == 0:
                res.append(curr)
            if left >0:
                help(left-1,right,curr+"(")
            if right >0 and left<right:
                help(left,right-1,curr+")")

        help(n-1,n,"(")

        return res


            
        