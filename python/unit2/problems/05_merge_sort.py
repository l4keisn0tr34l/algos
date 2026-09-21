"""
Problem: Merge Sort

Given an array of integers, sort it in ascending order using Merge Sort.
Modify the array in-place.

Example:
Input:  arr = [8, 3, 2, 9, 7, 1]
Output: [1, 2, 3, 7, 8, 9]

Expected Complexity: O(n log n)
"""


def merge(arr, low, mid, high):
    temp = []

    i = low
    j = mid+1

    while ( i<=mid and j<=high):
        if arr[i]<=arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1

    while ( i<=mid):
        temp.append(arr[i])
        i+=1
    while ( j<=high):
        temp.append(arr[j])
        j+=1
    for i in range(low, high+1):
        arr[i]=temp[i-low]
        
    

def merge_sort(arr, low, high):
    if low>=high:
        return
    mid = int((low+high)/2)
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr,low,mid,high)


if __name__ == "__main__":
    arr = [8, 3, 2, 9, 7, 1]
    merge_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 7, 8, 9]
    print("All tests passed")
