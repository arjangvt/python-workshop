# ***********************************
#  string1.pr
#  CCAM Workshop - 2017
#  Written by Arjang Fahim
#
# ***********************************

"""
In this program, we will find the largest number of 
three variables a, b and c
"""

# defining three variables
a = 30 
b = 10
c = 1
largest = 0

if a > b:
    largest = a
else:
    largest = b

if c > largest:
        largest = c

print ("The largest number is: " + str(largest))