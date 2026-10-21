class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((w, v))
            adj[v].append((w, u))

        mod = 10**9 + 7
        minheap = [(0, 0)]
        min_cost = [float("inf")] * n
        path_count = [0] * n
        path_count[0] = 1

        while minheap:
            cost, node = heapq.heappop(minheap)

            for nei_cost, nei in adj[node]:
                if cost + nei_cost < min_cost[nei]:
                    min_cost[nei] = cost + nei_cost
                    path_count[nei] = path_count[node]
                    heapq.heappush(minheap, (cost + nei_cost, nei))

                elif cost + nei_cost == min_cost[nei]:
                    path_count[nei] = (path_count[nei] + path_count[node]) % mod

        return path_count[n-1]