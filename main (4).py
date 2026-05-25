weight = input('''this program will conver your weight 
if you will put it in kilo tthe output will be in pounds 
& if you'll enter your weight in pound you will get output in kilos
" now enter your weight" :-''')

scale=input('''enter the scale " enter 'P' if it is in pound else enter K if it is in kilos" :- ''')

if(scale=="P"):
    weight_K= float(weight) * 0.45
    print('your weight is ', weight_K,'kilos')
elif(scale=="K"):
    weight_p= float(weight) / 0.45
    print('your weight is ',weight_p,'lbs')
else:
    print('please enter a valid scale')
