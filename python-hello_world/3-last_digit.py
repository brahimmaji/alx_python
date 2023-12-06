#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
thelastnumber=str(number)
thelastnumber=thelastnumber[-1]
print("Last digit of" ,number, "is" ,thelastnumber .format(number,thelastnumber))

#if the last digit is greater than 5: the string and is greater than 5
if int(thelastnumber) > 5 : 
    print("Last digit of" ,number, "is" ,thelastnumber ,"and is grater than 5".format(number,thelastnumber))

#if the last digit is 0: the string and is 0
if int(thelastnumber) == 0 :
    print("Last digit of" ,number, "is" ,thelastnumber ,"and is 0 ".format(number,thelastnumber))

#if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
if int(thelastnumber) < 6 and int(thelastnumber)!= 0 :
    print("Last digit of" ,number, "is" ,thelastnumber ," and is less than 6 and not 0 ".format(number,thelastnumber))
