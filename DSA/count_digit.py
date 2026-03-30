#count digits
def count_digits(num):
    """Return the number of digits in an integer (absolute value)."""
    num = abs(num)
    if num == 0:
        return 1
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count


if __name__ == "__main__":
    try:
        n = int(input("Enter an integer: "))
        print(f"Digit count: {count_digits(n)}")
    except ValueError:
        print("Please enter a valid integer.")