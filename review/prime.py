
num=eval(input("Enter the number that you want to know it is prime or not"))

start=1
count=0
for i in range(start,num+1) :
    if (num %i ==0) :
        count=count+1
    

if( count==2) :
    print(" Yes !!, the number "," ",num, "is a prime number ")


else :
    print("it is not prime number ")