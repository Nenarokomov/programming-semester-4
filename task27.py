import copy

def bubblesort(arr):
    for idx, _ in enumerate(arr):
        for j, _ in enumerate(arr):
            if arr[idx] > arr[j]:
                arr[idx], arr[j] = arr[j], arr[idx]


def qsort(arr, first, last):
    if first >= last:
        return

    idx, j = first, last
    pivot = arr[first]

    while idx <= j:
        while arr[idx] < pivot:
            idx += 1
        while arr[j] > pivot:
            j -= 1
        if idx <= j:
            arr[idx], arr[j] = arr[j], arr[idx]
            idx, j = idx + 1, j - 1
    qsort(arr, first, j)
    qsort(arr, idx, last)


def print_arr(arr):
    for idx, j in enumerate(arr):
        print(idx, j)
    print()


def main(init_arr):
    arr = copy.copy(init_arr)
    bubblesort(arr)
    print_arr(arr)

    arr = copy.copy(init_arr)
    qsort(arr, 0, len(arr) - 1)
    print_arr(arr)


