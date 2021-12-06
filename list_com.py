mylist=[]

x= input()
y= input()
z= input()
n= input()

t= n*(n-1)
for a in range(n*n):
    for b in range(x):
        for c in range(y):
            for d in range(z) :
                mylist.append(b,c,d)


print(mylist)