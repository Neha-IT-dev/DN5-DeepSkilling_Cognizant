#Insertion_sort


def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        temp=arr[i]
        j=i-1
        while(j>=0 and arr[j]>temp):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
if __name__=="__main__":
    arr = [8, 2, 6, 5, 3, 4]
    insertion_sort(arr)
    for i in range(len(arr)):
        print(arr[i],end=" ")


#time complexity= worstcase-->O(n^2) already sorted(bestcase)-->O(n)averagecase-->O(n^2)
#space complexity = O(1)  (no extra memory)
#stable
#in place



        




