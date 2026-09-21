"""Reference solution: Huffman Coding"""
import heapq

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
    def __lt__(self, other):
        return self.freq < other.freq

def build_codes(root, path, codes):
    if root is None:
        return
    if root.char is not None:
        codes[root.char] = path or "0"
        return
    build_codes(root.left, path + "0", codes)
    build_codes(root.right, path + "1", codes)

def huffman_codes(chars, freq):
    heap = [Node(f, c) for c, f in zip(chars, freq)]
    heapq.heapify(heap)
    while len(heap) > 1:
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        heapq.heappush(heap, Node(x.freq + y.freq, None, x, y))
    codes = {}
    build_codes(heap[0], "", codes)
    return codes

if __name__ == "__main__":
    codes = huffman_codes(['a','b','c','d','e','f'], [5,9,12,13,16,45])
    assert set(codes.keys()) == set(['a','b','c','d','e','f'])
    print(codes)
