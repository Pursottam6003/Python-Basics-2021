n=int(input())


mylist=[]
mynewlist=[]

for a in range(n):
    i=int(input())
    mylist.append(i)
    if mylist.count(i) ==1 :
        mynewlist.append(i)




l=len(mynewlist)
mynewlist.sort()
 
print(mynewlist[l-2])