'''
def hcf_func(a,b) :
    first=1
    end = min(a,b)

    for i in range(first,end+1) :
        
        if a%i==0 and b%i==0 :

            hcf=i  
        #printing the hcf 
    
    print("The HCF is ",hcf)



a,b=eval(input("Enter the two numbers "))
#calling the function
hcf_func(a,b)
     


'''
#we can also creat the same function and return the hcf and we will print them in main function


def hcf_func(a,b) :
    first=1
    end = min(a,b)

    for i in range(first,end+1) :
        
        if a%i==0 and b%i==0 :

            hcf=i  
       
    #return the function and we will print in outside the funcion 
    return hcf


a,b=eval(input("Enter the two numbers "))

#calling the function and storing the result
result = hcf_func(a,b)

print("The hcf is ",result)

