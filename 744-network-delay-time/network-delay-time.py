
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        
        import heapq
        min_heap = [(0, k)]  # (time, node)
        dist = {}
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in dist:
                continue
            dist[node] = time
            
            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(min_heap, (time + weight, neighbor))
        
        if len(dist) != n:
            return -1
        
        return max(dist.values())   