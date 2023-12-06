#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
thelastnumber=str(number)
thelastnumber=thelastnumber[-1]
print("Last digit of" ,number, "is" ,thelastnumber .format(number,thelastnumber))

if int(thelastnumber) > 5 : 
    print("Last digit of" ,number, "is" ,thelastnumber ,"and is grater than 5".format(number,thelastnumber))

if int(thelastnumber) == 0 :
    print("Last digit of" ,number, "is" ,thelastnumber ,"and is 0 ".format(number,thelastnumber))

if int(thelastnumber) < 6 and int(thelastnumber)!= 0 :
    print("Last digit of" ,number, "is" ,thelastnumber ," and is less than 6 and not 0 ".format(number,thelastnumber))
