#code

address,pincode= input("").split(",") #used to get string as input


if len(pincode)==6 :
    print(int(pincode))
    
else :
    print("0")
