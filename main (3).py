name= input('''please enter your name 
(please make sure that the name you enter ) :- ''')

if(len(name)<3):
    print(''' the name you netred is 
    lessthan 3 latters please reenter it again''')
elif(len(name)>50):
    print('the name can only be valid bitween 3 to 50 latters so please try entering your name a bit smaller')
else:
    print('the name you entered is given below\n',name)