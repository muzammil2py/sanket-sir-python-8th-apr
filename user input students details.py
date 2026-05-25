def sthudent_details():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    grade = input("Enter your grade: ")
    
    print(f"Student Name: {name}")
    print(f"Student Age: {age}")
    print(f"Student Grade: {grade}")

a=int(input("""how many students are there in the class:- """))

for i in range (a):

    student_details()
