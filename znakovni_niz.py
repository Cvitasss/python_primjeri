a=input('Unesi znakovni niz koji pretražuješ: ')
b=input('Unesi slovo koje tražiš? ')
nova=[]
for i in range(len(a)):
    if a[i]==b:
        nova.append(i)
if nova==[]:
    print('Slovo',b,'se ne pojavljuje u tekstu.')
else:
    print('Slovo',b,'se pojavljuje na slijedećim pozicijama',nova)