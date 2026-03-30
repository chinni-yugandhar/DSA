#count even digits 
#n = 1234567890
# o/p = 5    
def count_even_digits(n):
    count = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            count += 1
        n //= 10
    return count        
n = 1234567890
print(count_even_digits(n))       