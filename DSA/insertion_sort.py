def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        #shifting elements
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            arr[j + 1] =key
        return arr
arr = [9,4,2,7]
print(insertion_sort(arr)) 
   