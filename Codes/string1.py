# ***********************************
#  string1.pr
#  CCAM Workshop - 2017
#  Written by Arjang Fahim
#
# ***********************************

my_name = 'My name is Arjang Fahim'

print ("Printing the my_name value \n")
print (my_name + '\n')
print (my_name[3] + " " + my_name[5] + '\n')

# using function length
string_length =  len(my_name)
print ("The length of the sentence is " + str(string_length))

# slicing a string
sub_string1 = my_name[3:7]
print (sub_string1 + '\n')

# lowercase and uppercase
sub_string1 = my_name.lower()
print (sub_string1 + '\n')

sub_string1 = my_name.upper()
print (sub_string1 + '\n')