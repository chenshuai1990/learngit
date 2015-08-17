a=[1,2,3]
b=[1,3,5]
lst_and=[]
lst_or=[]

for i in a:
  if i in b:
    lst_and.append(i)
print lst_and

lst_or=b
for i in a:
  if i not in b:
    lst_or.append(i)

print lst_or


