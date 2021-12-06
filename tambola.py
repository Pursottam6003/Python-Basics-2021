

import random
import time

#initialize the list from 1 to 90
num=list(range(1,91))

phrases=[""]

#shuffle the list
random.shuffle(num)
print("After shuffling")


#tramsverse the list 

for i in num :
    print(i)
    time.sleep(2)
