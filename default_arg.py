def ask_ok(prompt,retries=4,reminder='please try again'):
    while True:
        ok= input(prompt) #from user 
        if ok in ('y','Y','ye','yes'):
            return True 
        
        if ok in ('n','no','nop','nope'):
            return False
        
        retries =retries-1

        if retries <0:
            raise ValueError('invalid user response')
        
        print(reminder)

ask_ok('y',3,"please")