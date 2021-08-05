def isPrime(num) :
    
    #assuming the number is prime already
    isPrime=True

    for i in range(2,int(num**0.5)) :
        if(num %i ==0) :
            isPrime=False

            break

    #condition while printing 
    #if statement executes only when the statemwnt inside if is true'
    if(isPrime) :
        print("Yes it is Prime number")

    else :
        print("No it is not prime number")


#user input
num=eval(input(""))

#calling the function 

isPrime(num)


'''
def isPrime(num) :
    
    #assuming the number is prime already
    isPrime=True

    for i in range(2,int(num**0.5)) :
        if(num %i ==0) :
            isPrime=False

            break

    #condition while printing 
    #if statement executes only when the statemwnt inside if is true'
    if(isPrime) :
        return True
       
    else :
        return False
        


#user input
num=eval(input(""))

#calling the function 

result = isPrime(num)

if result==True :
    print("Yes it is prime number")

else :
    print("No it is not prime number")



   



'''


   
