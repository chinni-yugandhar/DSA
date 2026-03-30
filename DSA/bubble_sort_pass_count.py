def bubble_sort_pass_count(arr):
    n=len(arr)
    count = 0

    for i in range(n):
        swapped =False

        for j in range(0, n-i -1):
            if arr[j]<arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swapped = True

                count +=1
                if not swapped:
                    break
                return count
            
arr=[8,4,2,6]
print(bubble_sort_pass_count(arr))
           