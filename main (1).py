name = input('enter your name please :- ')
age = input('now enter your age')
visits = input('now enter your past visits ao wecan know that you are a new patiant or existing ')

if(int(visits)<1):

    print("you're a new petiant")
    prob = input('''please write your problems here 
    so we can know what is going on with you''')

else:
    print("you're an existing patient")
    
    print(''' please call to our clinic to get an appointment''')
    app=input('please enter the desired time for your appointment(please enter time in 24 hour time ratio)')
    if(int(app)<=12):
        print('your appointment will be declared soon')
        
    else:
        print('please enter time after 12 pm')