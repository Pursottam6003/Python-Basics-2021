'''                           
sum = 0
item = 0
while item < 5:
    item += 1
    sum += item
    if sum > 4: break
print(sum)   '''
'''
number = 25
isPrime = True
i = 2 
while i < number and isPrime:
    if number % i == 0:
        isPrime = False
    i += 1
print("i is", i, "isPrime is", isPrime) 
'''
number = eval(input("Enter an integer: "))
isPrime = True
for i in range(2, number):
    if number % i == 0:
        isPrime = False
    print("i is", i)
    if isPrime:
        print(number, "is prime")
        break
    else:
        print(number, "is not prime")