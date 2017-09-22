# ***********************************
#  string1.pr
#  CCAM Workshop - 2017
#  Written by Arjang Fahim
#
# ***********************************

"""
This program calculates the sum of numbers [1 .. n]
n is given as input
"""

my_input = input ("Please enter an integer larger than 0:")
n = int(my_input)

if n <= 0:
	print ("Wrong input!\n")
	exit(0)

counter = 1
sum_num = 0
while counter <= n:
	sum_num = sum_num + counter
	counter += 1

print ("The sum of the integers between 1 to " + str(n) + " is " + str(sum_num))