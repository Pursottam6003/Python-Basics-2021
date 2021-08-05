
a,b= eval(input("Enter the number "))

#we will find the maximum number between them

start=1
end = max(a,b)


for i in range(start,end+1) :
    if (a % i ==0 and b % i==0) :
        hcf=i

lcm=a*b/hcf


print(int(lcm))
