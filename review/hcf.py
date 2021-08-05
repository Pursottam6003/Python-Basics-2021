
#we are creating hcf of two numbers only
#let us take two numbers a and b

a,b=eval(input(""))

#we will start from 1 as to avoid error of zeroes

first=1

#identifying min number between a and b

end = min(a,b)

for i in range(first,end+1) :
    if a%i==0 and b%i==0 :
        hcf=i
    

#printing the hcf 
print(hcf)
     



