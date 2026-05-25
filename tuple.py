asd=('apple','mango','kiwi','watermelon','melon')

'''print(asd)
print(asd[0])
print(asd[-1])
print(asd[1:4])
print(asd[1:])
print(asd[:4])
print(asd[:])'''

print(len(asd))

print(asd)
if 'gvava' in asd:
    print('yes')
else:
    print('no')

print(asd)
for x in range(len(asd)):
    if asd[x]=='kiwi':
        continue
    print(asd[x])