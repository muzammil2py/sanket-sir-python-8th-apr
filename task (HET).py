import datetime
x=datetime.datetime.now()

import random
y=random.randint(111, 999)
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    city = input("Enter student city: ")
    
    print('-----------------------------')
    print(x)
    print(y)
    print(f"Student Name: {name}")
    print(f"Student City: {city}")
    print('-----------------------------')