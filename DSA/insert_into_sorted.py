#  approach
#start from end of an array
#shift elements greater than x
#insert x in correct position
def insert_into_sorted(arr, x):
    arr.append(0) #ADD space for new element
    i=len(arr) - 2 #starting from last oroginal
    #shifting element to right
    while i>=0 and arr[i] > x:
        arr[i+1] = arr[i]
        i -= 1
        #insert x
        arr[i+1] = x
        return arr
arr = [1,3,5,7 ]
x = 4
print(insert_into_sorted(arr, x))