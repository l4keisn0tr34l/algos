"""
Lab 07: Huffman Coding
"""

import heapq


class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def generate_codes(root, code, codes):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = code or "0"
        return

    generate_codes(root.left, code + "0", codes)
    generate_codes(root.right, code + "1", codes)


def huffman(chars, freq):
    heap = []
    for c, f in zip(chars, freq):
        heapq.heappush(heap, Node(f, c))

    while len(heap) > 1:
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        z = Node(x.freq + y.freq, None, x, y)
        heapq.heappush(heap, z)

    root = heap[0]
    codes = {}
    generate_codes(root, "", codes)
    return codes


def average_code_length(codes, freq, chars):
    total_freq = sum(freq)
    total = 0
    for c, f in zip(chars, freq):
        total += f * len(codes[c])
    return total / total_freq


if __name__ == "__main__":
    chars = ["a", "b", "c", "d", "e", "f"]
    freq = [5, 9, 12, 13, 16, 45]
    codes = huffman(chars, freq)

    print("Codes:", codes)
    print("Average length:", average_code_length(codes, freq, chars))
