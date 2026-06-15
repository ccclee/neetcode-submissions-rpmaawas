class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch]={}
                node = node[ch]
            node["words"] = word
        row = len(board)
        col = len(board[0])
        res =[]

        def dfs(r,c,node):
            if not (0<=r<row and 0<=c<col):
                return 
            ch = board[r][c]
            if ch not in node:
                return 
            nextnode = node[ch]

            if "words" in nextnode:
                res.append(nextnode["words"])
                del nextnode["words"]

            board[r][c] ="#"

            dfs(r+1,c,nextnode)
            dfs(r,c+1,nextnode)
            dfs(r-1,c,nextnode)
            dfs(r,c-1,nextnode)

            board[r][c] = ch

            if not nextnode:
                del node[ch]

        for c in range(col):
            for r in range(row):
                dfs(r,c,trie)
        return res

            