class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_lst = [[] for _ in range(n)]
        for u, v in edges:
           adj_lst[u].append(v)
           adj_lst[v].append(u) 
        
        visited = [0 for _ in range(n)]
        cnt = 0

        def dfs(node):
            visited[node] = 1
            for i in adj_lst[node]:
                if visited[i] == 1:
                    continue
                dfs(i)

        for i in range(len(visited)):
            if visited[i] == 0:
                cnt += 1
                dfs(i)

        return cnt