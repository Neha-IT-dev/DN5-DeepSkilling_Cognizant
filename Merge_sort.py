#Mergesort

def merge(A, lb, mid, ub):

    B = [0] * len(A)

    i = lb
    j = mid + 1
    k = lb

    while i <= mid and j <= ub:

        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1

        k += 1

    while i <= mid:
        B[k] = A[i]
        i += 1
        k += 1

    while j <= ub:
        B[k] = A[j]
        j += 1
        k += 1

    for k in range(lb, ub + 1):
        A[k] = B[k]


def mergeSort(A, lb, ub):

    if lb < ub:

        mid = (lb + ub) // 2

        mergeSort(A, lb, mid)

        mergeSort(A, mid + 1, ub)

        merge(A, lb, mid, ub)


if __name__ == "__main__":

    A = [15, 5, 24, 8, 1, 3, 16, 10, 20]

    mergeSort(A, 0, len(A) - 1)

    print("Sorted Array:")

    for i in range(len(A)):
        print(A[i], end=" ")


"""time complexity : O(nlogn) for all  3cases
space complexiry: O(n)
stable
not in place"""
