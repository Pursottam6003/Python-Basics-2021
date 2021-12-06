n=int(input())


 
second_max=-1
first_max=0
for a in range(n):
        s=int(input())
        '''
            if(s>first_max):
                
                second_max=first_max
                first_max=s
        '''

        if(s>first_max and s>second_max):
            if first_max >second_max :
                second_max=first_max
                first_max=s

print(second_max)
print(first_max)
        

 


 
