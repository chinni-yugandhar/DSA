#count digits in a number
#n = 12345      
# o/p = 5
def count_digits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count
n = 12345
print(count_digits(n))      
