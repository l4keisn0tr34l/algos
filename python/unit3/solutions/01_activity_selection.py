"""Reference solution: Activity Selection"""

def activity_selection(activities):
    activities = sorted(activities, key=lambda x: x[1])
    selected = []
    last_finish = float('-inf')
    for start, finish in activities:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish
    return selected

if __name__ == "__main__":
    acts = [(1,4), (3,5), (0,6), (5,7), (8,9), (5,9)]
    assert activity_selection(acts) == [(1,4), (5,7), (8,9)]
    print("All tests passed")
