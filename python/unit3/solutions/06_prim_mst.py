"""Reference solution: Prim MST"""
import heapq

def prim_mst(adj, start=0):
    V = len(adj)
    visited = [False] * V
    heap = [(0, start, -1)]
    total = 0
    mst = []
    while heap and len(mst) < V - 1:
        w, u, parent = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total += w
        if parent != -1:
            mst.append((parent, u, w))
        for v, wt in adj[u]:
            if not visited[v]:
                heapq.heappush(heap, (wt, v, u))
    return total, mst

if __name__ == "__main__":
    adj = [[(1,10),(2,6),(3,5)],[(0,10),(3,15)],[(0,6),(3,4)],[(0,5),(1,15),(2,4)]]
    weight, mst = prim_mst(adj, 0)
    assert weight == 19 and len(mst) == 3
    print("All tests passed")
