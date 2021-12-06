''' write a program to print the dictionary words in hindi and enlish'''

myDict={
    "aaam" :" mango",
    "chasma" :"specticles",
    "muli" :"ragish",
    "pankha":"fan",
    "chamkadaar":"bat"
}

print(myDict.keys())

a=input("Enter the option for the language in hindi : ")

print(myDict.get(a))

