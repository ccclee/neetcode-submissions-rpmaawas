class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[]for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node,parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor,node)
        
        count = 0
        visited = set()

        for node in range(n):
            if node not in visited:
                count+=1
                dfs(node,-1)

        return count
                
        