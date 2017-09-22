# ***********************************
#  string1.pr
#  CCAM Workshop - 2017
#  Written by Arjang Fahim
#
# ***********************************

# example of a list
list1 = [1, 2, 3, 4, 5]
print (list1)

print (type(list1))

print (dir(list1))

# concatenation of two lists
list2 = list1 + [6, 7, 8]
print (list2)

# accessing to an element by index
print ("The item at index 2 is " + str(list2[2]))

# remove the first item from list
index = 4
pop_item = list2.pop(index)
print ("The item at index " + str(index) + " is " + str(pop_item))
print ("The list after pop-up an item:\n ")
print (list2)


list2 = [1, 1, 2, 2, 2, 3, 3]
# counting the list items
print ("The count of number 2 in the list is " + " " + str(list2.count(2)))

# sorting the list
list3 = [2, 5, 1, 0, 10, 7]
list3.sort() 
print (list3)


# list of lists 

list1 = [[1, 2], [4, 5], [6, 7]]
print (list1)

# print an item by index 
print (list1[2][1])
print (list1[0][1])