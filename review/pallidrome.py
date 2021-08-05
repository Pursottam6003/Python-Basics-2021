
#prompt the user to enter a steing
s= input("Emter the string")

#make the start to 0

start=0

#making the end to the uppmost charecter

end = len(s) -1


#compare the characters of start and end : start < end

while start < end :

    if  s[start]==s[end] :


        start=start+1
        end=end-1
    else :

        break

if start < end :
    print("Not pallindrome")

else :
    
    print("pallildrome")