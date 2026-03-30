#Fee Calculator
def calculate_fee(course,marks):
    if course == "AI":
        fee = 50000
    elif course == "Web Development":
        fee = 60000
    elif course == "Data Science":  
        fee = 70000
    else:
        return None #"Invalid course"
    #Discount condition
    if course == "AI" and marks >= 80:
        fee -= 5000
    return fee

def main():
    course = input("Enter the course (AI, Web Development, Data Science): ")
    marks = int(input("Enter your marks: "))
    fee = calculate_fee(course, marks)
    if fee is None:
        print("Invalid course")
    else:
        print("Final fee:", fee)

main()              
        
            

    