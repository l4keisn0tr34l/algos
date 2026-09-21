"""Reference solution: Minimum CDs"""
def min_cds(songs, m):
    cds = 1
    remaining = m
    for song in songs:
        if song > m:
            return -1
        if song <= remaining:
            remaining -= song
        else:
            cds += 1
            remaining = m - song
    return cds

if __name__ == "__main__":
    assert min_cds([4, 3, 5, 2, 1], 7) == 3
    assert min_cds([8, 1], 7) == -1
    print("All tests passed")
