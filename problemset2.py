#!/usr/bin/env python3
import sys

my_value= int(sys.argv[1])
print (f"the value you chose was {my_value}")
# if my_value :
# 	print("true")
# else:
# 	print ("not true")

if my_value >0:
	print('positive')
	isit_lt50= my_value <50
	if my_value <50:
		if my_value%2 == 0:
				print ("the number is even and less than 50")
	elif my_value>50:
		if my_value%3==0:
			print("larger than 50, divisible by 3")
	else:
		print("the number is 50")
      
elif my_value<0:
     print('negative')
else:
    print ("the number is 0")
