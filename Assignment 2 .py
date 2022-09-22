#!/usr/bin/env python
# coding: utf-8

# #1.What are the two values of the Boolean data type? How do you write them?

# In[ ]:


# ans- Two values of the Boolean data type is "TRUE" and "FALSE". The right method to right it is True, False (means first letter T & F are capital remaining in small)


# #2. What are the three different types of Boolean operators?

# In[ ]:


# ans:- Three different types of Boolean operators are or, and, and not


# #3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

# In[ ]:


#ans:- 
True and True = True.

True and False = False.

False and True = False.

False and False = False.

True or True = True.

True or False = True.

False or True = True.

False or False = False.

not True = False.

not False = True.


# #4. What are the values of the following expressions?
# (5 > 4) and (3 == 5)
# not (5 > 4)
# (5 > 4) or (3 == 5)
# not ((5 > 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)

# In[ ]:


#ans:- 
(5 > 4) and (3 == 5)                = False
not (5 > 4)                         = False
(5 > 4) or (3 == 5)                 = True
not ((5 > 4) or (3 == 5))           = False
(True and True) and (True == False) = False
(not False) or (not True)           = True


# #5. What are the six comparison operators?

# In[ ]:


# Ans:- six comparison operators are (<, >, <=, >=, ==, !=)


# #6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

# In[7]:


#Ans:- == is the equal to operator that compares two values and evaluates to a Boolean (True & False), while = is the assignment operator that stores a value in a variable. 
# A condition is an expression used in a flow control statement that evaluates to a Boolean value.

a = int(input("first value"))
if a == 6:
    a= a+1
    print(a)
else :
    print("heelo")


# #7. Identify the three blocks in this code:
# spam = 0
# if spam == 10:
# print('eggs')
# if spam > 5:
# print('bacon')
# else:
# print('ham')
# print('spam')
# print('spam')
# 

# In[8]:


#ans:
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')


# #8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

# In[12]:


spam = int(input("value "))
if spam == 1:
    print("hello")
    if spam == 2:
        print("Howdy")
else:
    print("Greetings!")


# #9.If your programme is stuck in an endless loop, what keys you’ll press?

# In[ ]:


#ans:- interrupt the Kernel and restart again


# #10. How can you tell the difference between break and continue?

# In[ ]:


ans:- break statement used for exit the entire loop. The continue statement will move the execution to the start of the loop.


# #11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

# In[ ]:


# ans:- there is no difference between range(10), range(0, 10), and range(0, 10, 1), they all are smae.The range(10) call ranges from 0 up to 9, range(0, 10) explicitly tells the loop to start at 0 & end with 9, and range(0, 10, 1) explicitly tells the loop to increase the variable by 1 on each iteration.
range(10)


# In[2]:


range(0, 10)


# In[3]:


range(0, 10, 1)


# #12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[3]:


for i in range(1,11):
    print(i)


# In[1]:


i = 1
while i <=10:
    print(i)
    i = i+1


# #13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

# In[ ]:


#Ans:- spam.bacon()

