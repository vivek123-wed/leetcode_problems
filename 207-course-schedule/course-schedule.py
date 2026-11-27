class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites: graph[b].append(a)
        visited = set()
        def dfs(i):
            if i in visited: return False
            if not graph[i]: return True
            temp, graph[i] = graph[i], []
            visited.add(i)
            if not all(dfs(j) for j in temp): return False
            visited.remove(i)
            graph[i] = []
            return True
        return all(dfs(i) for i in range(numCourses))