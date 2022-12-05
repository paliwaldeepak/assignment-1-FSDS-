#!/usr/bin/env python
# coding: utf-8

# 1. What advantages do Excel spreadsheets have over CSV spreadsheets?

# #ans:- The Advantages of Excel over CSV are:
# 
# 1.Excel (XLS and XLSX) file formats are better for storing and analysing complex data.
# 2.An Excel not only stores data but can also do operations on the data using macros, formulas etc
# 3.CSV files are plain-text files, Does not contain formatting, formulas, macros, etc. It is also known as flat files

# 2. What do you pass to csv.reader() and csv.writer() to create reader and writer objects?

# In[4]:


#ans:- 
import csv
with open('haberman.csv','r') as file:
    csv_file = csv.reader(file,delimiter=',')
    for X in csv_file:
        print(X)


# 3. What modes do File objects for reader and writer objects need to be opened in?

# #ans:-  For csv.reader(file_object), the file objects needed to be opened in read mode mode='r' Whereas for csv.writer(file_object) the file objects needed to be opened in write mode mode='w'

# 4. What method takes a list argument and writes it to a CSV file?

# #ans:- csv.writer class provides two methods for writing to CSV. They are writerow() and writerows(). writerow() method writes a single row at a time. Whereas writerows() method is used to write multiple rows at a time.

# 5. What do the keyword arguments delimiter and line terminator do?

# #ans:- Lets take the example of a csv file:
# First Name, Last Name, Age
# Mano, Vishnu, 24
# Vishnu, Vardhan, 21
# Here ',' is Delimiter. We can use any Character as per our needs if required. Similarly Line Terminator comes at end of line by default it is newline and can be changed accourding to Requirement.

# 6. What function takes a string of JSON data and returns a Python data structure?

# #ans:- loads() method takes a string of JSON data and returns a Python data structure

# 7. What function takes a Python data structure and returns a string of JSON data?

# #ans:- dumps() method takes a python data structure and returns a string of JSON data
