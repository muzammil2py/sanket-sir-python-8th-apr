students = {}

def studentinfo():
    a = int(input("How many students are there in the class? "))
    
    for i in range(a):
        print("\nStudent", i + 1)
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        email = input("Enter student email: ")
        phone = input("Enter student phone number: ")   
        
        # Store data simply in the dictionary
        students[id] = {"name": name, "email": email, "phone": phone}

def display_data():
    print("\n--- Student Table ---")
    print("ID \t Name \t\t Email \t\t Phone")

    # Loop through the dictionary to print
    for id in students:
    
        name = students[id]["name"]
        email = students[id]["email"]
        phone = students[id]["phone"]
        
        # Using basic commas to print variables and tabs (\t) together
        print(id, "\t", name, "\t", email, "\t", phone)

def search_data():
    find = input("\nEnter an ID or Name to search: ")
    
    for id in students:
        name = students[id]["name"]
        
        # Check if they typed the exact ID or Name
        if find == id or find == name:
            print("\nMatch Found!")
            print("ID:", id)
            print("Name:", name)
            print("Email:", students[id]["email"])
            print("Phone:", students[id]["phone"])
            return  # This stops the search function since we found the person
            
    

    print("\nStudent not found.")



studentinfo()
display_data()
search_data()