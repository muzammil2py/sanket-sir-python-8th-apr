correct_word=['m','u','z','a','m','m','i','l']

print('your hint',set(correct_word))

list(correct_word)

attemps=int(input('enter how many attemps you want to take'))

print('''WARNING : if attemps would be over you lose and the game will be automatically quitted''')


for i in range(attemps):
    guess=input('Enter you guessed word')
    if guess==correct_word:
        print('you win')
        break
    else :
        print('try again')
        attemps-=1
        print(f'you have {attemps} attemps left')   


