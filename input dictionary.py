slist=[]
adata={}
a=int(input('''enter the number of students'''))
b=int(input('''enter the number of elements'''))

for i in range(a):
    for j in range(b):
        key=input('enter the key')
        d=input('enter the value ')
        adata[key]=d
    slist.append(adata)

print(slist)