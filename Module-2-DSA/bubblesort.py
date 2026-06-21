#Bubble Sort

def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        swapped=False
        for j in range(n-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if(swapped==False):
            break
if __name__=="__main__":
    arr=[8,2,6,5,3,4]
    bubble_sort(arr)
    for i in range(len(arr)):
        print(arr[i],end=" ")



#time complexity= worstcase-->O(n^2) already sorted(bestcase)-->O(n)averagecase-->O(n^2)
#space complexity = O(1)  (no extra memory)
#stable
#in place
