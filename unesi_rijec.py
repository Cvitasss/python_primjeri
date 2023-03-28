a=input('Unesi riječ: ')
b=input('Koje slovo tražiš? ')
x=a.find(b)
if x==-1:
    print('Slova',b,'nema u riječi.')
else:
    print('Slovo',b,'je na poziciji',x)