a=input('Unesi brojeve: ').split()
b=[]
for i in range(len(a)):
    if int(a[i])%2==0:
        b.append(int(a[i]))
print(b)
