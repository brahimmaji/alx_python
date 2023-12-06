#Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)
i= range(0 , 99)
for n in i :
 print("{}=0x{}".format(n,n))