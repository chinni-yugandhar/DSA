#Finding sum of array elements
#arr = [1, 2, 3, 4, 5]
# o/p = 15
def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
arr=[1, 2, 3, 4, 5]
print(sum_of_array(arr))