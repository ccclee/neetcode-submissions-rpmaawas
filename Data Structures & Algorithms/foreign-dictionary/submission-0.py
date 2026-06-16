class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chs = set()
        indegree = defaultdict(int)
        for word in words:
            for ch in word:
                chs.add(ch)
                indegree[ch]= 0

        graph = defaultdict(set)

        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            if len(word1)>len(word2) and word1[:len(word2)]== word2:
                return ""
            for i in range(min(len(word1), len(word2))):
                if word1[i]!= word2[i]:
                    if word2[i] not in graph[word1[i]]:
                        indegree[word2[i]]+=1
                        graph[word1[i]].add(word2[i])
                    break
        res =[]
        q = deque()
        for ch, count in indegree.items():
            if count ==0:
                q.append(ch)

        while q:
            ch = q.popleft()
            res.append(ch)
            for nei in graph[ch]:
                indegree[nei]-=1
                if indegree[nei] ==0:
                    q.append(nei)
        if len(res)!= len(chs):
            return ""
        return "".join(res)
        