#https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

mylist=[]
x= int(input())
y= int(input())
z= int(input())
n= int(input())


for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            if (a+b+c) !=n : 
                
            
                mylist.append([a,b,c])


            #[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
print(mylist)