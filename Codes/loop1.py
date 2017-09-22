# ***********************************
#  string1.pr
#  CCAM Workshop - 2017
#  Written by Arjang Fahim
#
# ***********************************

# example of a for loop
largest = 0
items = [2, 12, 67, 78, 73, 100]

for item in items:
    if item > largest:
        largest = item

print ("The largest number in the list is " + str(largest)) 