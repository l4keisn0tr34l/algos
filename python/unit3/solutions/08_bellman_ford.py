"""Reference solution: Bellman-Ford"""
def bellman_ford(V, edges, source):
    dist = [float('inf')] * V
    dist[source] = 0
    for _ in range(V - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None
    return dist

if __name__ == "__main__":
    V = 5
    edges = [(0,1,-1),(0,2,4),(1,2,3),(1,3,2),(1,4,2),(3,2,5),(3,1,1),(4,3,-3)]
    assert bellman_ford(V, edges, 0) == [0, -1, 2, -2, 1]
    print("All tests passed")
