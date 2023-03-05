a=input('Unesi ocjene: ').split()
b=[]
for i in range(len(a)):
    b.append(int(a[i]))
print(b.count(5),'su učenika dobila ocjenu odličan.')
print(b.count(4),'su učenika dobila ocjenu vrlo dobar.')
print(b.count(3),'su učenika dobila ocjenu dobar.')
print(b.count(2),'su učenika dobila ocjenu dovoljan.')
print(b.count(1),'su učenika dobila ocjenu nedovoljan.')
