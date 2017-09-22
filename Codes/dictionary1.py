# ***********************************
#  string1.pr
#  CCAM Workshop - 2017
#  Written by Arjang Fahim
#
# ***********************************

# example of a dictionary
my_dict = {}
my_dict = {'AJ':36, 'Zach':25, 'Tim':38, 'Andrew':25}
print (my_dict)

print ("printing the value with a key of three is "  + str(my_dict['Zach']))

# assignment of a value
my_dict['Zach'] = 30
print (my_dict)

del my_dict['Zach']
print (my_dict)

# the list of values
print (my_dict.items())


# the list of keys
print (my_dict.keys())

# the list of values
print (my_dict.values())