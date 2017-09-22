#!/usr/bin/python

"""

Functionality:
    This toolbox contains modules for text file manipulations.
    Many of the functionality of this toolbox can be delivered by using
    Linux command. This is useful for windows user.
  
dependencies: 
    FileTask version 1.0.0

Author: Arjang Fahim
Date created: 5/6/2017
Version: 1.0.0

"""

import sys
import glob

sys.path.append('../')

from Module.FileTask import FileTask


class TextFileTools:

    text_file_tools_count = 0

    def __init__(self, file_name, open_mode):

        """
        Constructor

        Keyword arguments:

        file_name -- the input file
        open_mode -- the file operation mode ('r', 'w' or 'a') 
        """

        self.ft = FileTask(file_name, open_mode)
        self.ft.readFile()
        self.data = self.ft.getData()


    def columnRemove(self, column_number, new_file_name):

        """
        This method removes a specified column from a file.

        Keyword arguments:

        column_number: the index of column that is removed
        new_file_name: the name of a new file 
        """

        data = ""
        for line in self.data:
            words = line.split()
            if (column_number == 1):
                words = words[1:]
            else:
                first_half = words[0:column_number]
                second_half = words[column_number+1:]
                words = first_half + second_half

            data = data + ' '.join(words) + "\n"

        ft = FileTask(new_file_name, 'w')
        ft.writeFile(data) 

    def columnsRangeRemove(self, column_start, column_end, new_file_name):

        """
        """

        data = ""
        for line in self.data:
            words = line.split()
            first_half = words[:column_start -1 ]
            second_half = words[column_end-1:]
            words = first_half + second_half
            #print words
            data = ' '.join(words) + "\n"
            ft = FileTask(new_file_name,'a')
            ft.writeFile(data)

        #ft = FileTask(new_file_name, 'w')
        #ft.writeFile(data) 


    def columnAddBySum(self, column_number1, column_number2, new_file_name):

        """
        This method sums up two given column and saves the result into a new column.
        The new column is at the end.

        Keyword arguments:

        column_number1: the first column for adding
        column_number2: the second column for adding
        new_file_name: the name of a new file  
        """

        data = ""
        for line in self.data:
            words = line.split()
            col1 = words[column_number1]
            col2 = words[column_number2]
            sum_col = int(col1) + int(col2)
            words.append(str(sum_col))
            data = data + ' '.join(words) + "\n"

        ft = FileTask(new_file_name, 'w')
        ft.writeFile(data)

    def columnAddBySubtract(self, column_number1, column_number2, new_file_name, subtract_flag):

        """
        This method subtract two given column and saves the result into a new column.
        The new column is at the end.

        Keyword arguments:

        column_number1: the first column for adding
        column_number2: the second column for adding
        new_file_name: the name of a new file
        subtract_flag:  if its 1 then column1 - column2 and if its 2 otherwise
        """

        data = ""
        for line in self.data:
            words = line.split()
            
            col1 = words[column_number1]
            col2 = words[column_number2]
            try:
                if subtract_flag == 1:
                     result_col = float(col1) - float(col2)
                else:
                     result_col = float(col2) - float(col1)

            except(ValueError):
                print words
                pass

            words.append(str(result_col))
            data = data + ' '.join(words) + "\n"
            print words

        ft = FileTask(new_file_name, 'w')
        ft.writeFile(data)



    def columnAddRowCounter(self, where_to_add_index, new_file_name, is_first_row_title):

        """
        This methods adds a new column that counts the number of rows.

        Keyword arguments:

        where_to_add_index: the index of the location that row count 
                            is added
        new_file_name: the name of a new file
        is_first_row_title: 1 for not including 
        """

        data = ""
        counter  = 1

        for line in self.data:
            if (is_first_row_title == 1):
                is_first_row_title = 0
                continue
            words = line.split()
            words.insert(where_to_add_index, str(counter))
            data = '\t'.join(words) + "\n"
            ft = FileTask(new_file_name,'a')
            ft.writeFile(data)
            counter += 1

    def columnAddFixChr(self, where_to_add_index, chr_index, new_file_name):

        """
        This method is used for changing the chr column to the desired format.

        Keyboard argumants:

        where_to_add_index: the index of new field position
        new_file_name: the name of new file
        """

        data = ""
        ft = FileTask(new_file_name, 'a')
       
        for line in self.data:
            words = line.split()
            chr_val = words[chr_index]
            chr_val = "chr" + chr_val
            words.insert(where_to_add_index, chr_val)
            data = ' '.join(words) + "\n"
            ft.writeFile(data)

        #ft = FileTask(new_file_name, 'w')
        #ft.writeFile(data)

    def mergeTextFiles(self, file_folder_path, merged_file_name, add_line_count):
        """
        pattern matching
        """
        file_list = glob.glob(file_folder_path)

        for file_item in file_list:
            print file_item

        
#    def writeNewFile(self, new_file_name):

        """
        """

#    def columnAdd(self, Data):
        """
        """
