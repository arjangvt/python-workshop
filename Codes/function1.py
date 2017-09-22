# ***********************************
#  string1.pr
#  CCAM Workshop - 2017
#  Written by Arjang Fahim
#
# ***********************************

def find_max(items):
    largest = items[0]
    for item in items:
        if item > largest:
            largest = item
    return largest

def find_min(items):
    smallest = items[0]
    for item in items:
        if item < smallest:
            smallest = item
    return smallest

def average(items):
	pass

def min_max(items):
    return find_max(items), find_min(items)


print (min_max([1,3,10,1000]))

