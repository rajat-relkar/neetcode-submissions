class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_lst = [[] for _ in range(n)]
        for u, v in edges:
          adj_lst[u].append(v)
          adj_lst[v].append(u)

        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False
             
            visit.add(node)

            for i in adj_lst[node]:
                if i == parent:
                    continue
                if not dfs(i, node):
                    return False
            return True

        if dfs(0, -1) and len(visit) == n:
            return True
        else:
            return False
        