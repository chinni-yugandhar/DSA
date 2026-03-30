#checking the number even or odd
def even_or_odd(number):
    if number % 2 == 0:
        print ("Even")
    else:
        print ("Odd")
def main():     
    number = int(input("Enter a number: "))
    even_or_odd(number)         
    main()    