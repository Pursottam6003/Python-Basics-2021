a,b=eval(input("Enter two numbers seperated by ,"))

r=a%b

while r!=0 :


    a,b=b,r

    r=a%b
print("HCF is ",b)

