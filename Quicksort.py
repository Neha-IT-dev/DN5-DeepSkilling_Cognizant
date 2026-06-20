#Quicksort


def partition(A, lb, ub):

    pivot = A[lb]

    start = lb
    end = ub

    while start < end:

        while start <= ub and A[start] <= pivot:
            start += 1

        while A[end] > pivot:
            end -= 1

        if start < end:
            A[start], A[end] = A[end], A[start]

    A[lb], A[end] = A[end], A[lb]

    return end


def quickSort(A, lb, ub):

    if lb < ub:

        loc = partition(A, lb, ub)

        quickSort(A, lb, loc - 1)

        quickSort(A, loc + 1, ub)


if __name__ == "__main__":

    A = [7, 6, 10, 5, 9, 2, 1, 15, 7]

    quickSort(A, 0, len(A) - 1)

    print("Sorted Array:")

    for i in range(len(A)):
        print(A[i], end=" ")



"""
Time Complexity:
Best Case    : O(n log n)
Average Case : O(n log n)
Worst Case   : O(n²)
Space Complexity: O(log n)
not stable
inplace """
