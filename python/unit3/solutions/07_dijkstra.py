"""Reference solution: Dijkstra"""
import heapq

def dijkstra(adj, source):
    V = len(adj)
    dist = [float('inf')] * V
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist

if __name__ == "__main__":
    adj = [[(1,4),(2,1)],[(3,1)],[(1,2),(3,5)],[]]
    assert dijkstra(adj, 0) == [0, 3, 1, 4]
    print("All tests passed")
