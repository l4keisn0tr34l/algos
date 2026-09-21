"""
Problem: Huffman Coding

Given characters and frequencies, return a dictionary mapping each character to
its Huffman code.

Example:
Input: chars = ['a','b','c','d','e','f'], freq = [5,9,12,13,16,45]
Output: valid prefix-free Huffman codes

Expected Complexity: O(n log n)
"""


def huffman_codes(chars, freq):
    # TODO: build Huffman tree using min heap and return codes dictionary
    pass


if __name__ == "__main__":
    codes = huffman_codes(['a','b','c','d','e','f'], [5,9,12,13,16,45])
    assert isinstance(codes, dict)
    assert set(codes.keys()) == set(['a','b','c','d','e','f'])
    print("Codes:", codes)
