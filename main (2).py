print(' You want to buy a house woth 1 million')
credit=input('for checking the loan intrest please enter your credit score out of 900  :-')
if(int(credit)<=500):
    print('''your credit is  bad
    you need to pay intrest by 20%''')
else:
    print('''your credit is good  
    you have to pay intrest by 10% only''')